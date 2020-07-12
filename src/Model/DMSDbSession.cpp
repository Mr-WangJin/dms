#include "stdafx.h"
#include "DMSDbSession.h"

static const QString c_sAccessDatabaseName = "DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};FIL={MS Access};dbq=%1"; 
static const QString c_sField_RecNo = "#RecNo";

class MySqlDatabase : public QSqlDatabase
{
public:
    MySqlDatabase(const QString& type) :QSqlDatabase(type) {}
};

DMSDbSession::DMSDbSession(const QString &fileName, DatabaseType dbType)
    :m_sFileName(fileName), m_dbType(dbType)
{
    if (dbType == Access)
        m_db = MySqlDatabase("QODBC");
    else
        m_db = MySqlDatabase("QSQLITE");
}

DMSDbSession::~DMSDbSession()
{
    close();
}

QString DMSDbSession::fileName()
{
    return m_sFileName;
}

void DMSDbSession::setIsOutputSql(bool val)
{
    m_isOutputSql = val;
}

QSqlDatabase DMSDbSession::database() const
{
    return m_db;
}

QSqlError DMSDbSession::lastError() const
{
    return error;
}

bool DMSDbSession::open()
{
    close();
    if (m_dbType == Access)
        m_db.setDatabaseName(c_sAccessDatabaseName.arg(m_sFileName));
    else
        m_db.setDatabaseName(m_sFileName);
    if (m_db.open())
    {
        if (m_dbType == SQLite)
        {
            QSqlQuery editQuery(m_db);
            // 设置级联删除
            execSQL(editQuery, "PRAGMA foreign_keys = 1");
            // 提高写入数据的效率（效率优化非常明显）
            execSQL(editQuery, "PRAGMA synchronous = OFF");
        }
        return true;
    }
    else
    {
        qDebug() << m_db.lastError();
        return false;
    }
}

void DMSDbSession::close()
{
    if (m_db.isOpen())
        m_db.close();
}

bool DMSDbSession::transaction()
{
    return m_db.transaction();
}

bool DMSDbSession::commit()
{
    return m_db.commit();
}

bool DMSDbSession::rollback()
{
    return m_db.rollback();
}

void DMSDbSession::close_foreignKeys()
{
    m_db.exec("PRAGMA foreign_keys = 0");
}

void DMSDbSession::open_foreignKeys()
{
    m_db.exec("PRAGMA foreign_keys = 1");
}

QString DMSDbSession::sqlStatement(StatementType type, const QString &tableName,
    const QStringList &fieldNames) const
{
    int i;
    QString s;
    s.reserve(128);
    switch (type)
    {
    case SelectStatement:
        if (fieldNames.size() == 0)
            s.append(QLatin1String("*"));
        else
        {
            for (i = 0; i < fieldNames.count(); ++i)
            {
                if (fieldNames[i].isEmpty())
                    continue;
                if (fieldNames[i] == c_sField_RecNo)
                    continue;
                s.append(fieldNames[i]).append(QLatin1String(", "));
            }
            s.chop(2);
        }
        s.prepend(QLatin1String("SELECT ")).append(QLatin1String(" FROM ")).append(tableName);
        break;
    case WhereStatement:
        for (int i = 0; i < fieldNames.count(); ++i)
        {
            s.append(QLatin1String(i ? " AND " : "WHERE "));
            s.append(fieldNames[i]);
            s.append(QLatin1String(" = ?"));
        }
        break;
    case InsertStatement:
    {
        s.append(QLatin1String("INSERT INTO ")).append(tableName).append(QLatin1String(" ("));
        QString vals;
        for (i = 0; i < fieldNames.count(); ++i)
        {
            s.append(fieldNames[i]).append(QLatin1String(", "));
            vals.append(QLatin1Char('?'));
            vals.append(QLatin1String(", "));
        }
        if (vals.isEmpty())
            s.clear();
        else
        {
            vals.chop(2); // remove trailing comma
            s[s.length() - 2] = QLatin1Char(')');
            s.append(QLatin1String("VALUES (")).append(vals).append(QLatin1Char(')'));
        }
        break;
    }
    case DeleteStatement:
        s.append(QLatin1String("DELETE FROM ")).append(tableName);
        break;
    case UpdateStatement:
    {
        s.append(QLatin1String("UPDATE ")).append(tableName).append(QLatin1String(" SET "));
        for (i = 0; i < fieldNames.count(); ++i)
        {
            s.append(fieldNames[i]).append(QLatin1Char('='));
            s.append(QLatin1Char('?'));
            s.append(QLatin1String(", "));
        }
        if (s.endsWith(QLatin1String(", ")))
            s.chop(2);
        else
            s.clear();
        break;
    }
    default:
        break;
    }
    return s;
}

QString DMSDbSession::selectSqlStatement(const QString & tableName, const QStringList& fieldNames,
    const QStringList &wherefieldNames, const QString &orderBySql) const
{
    QString stmt = sqlStatement(SelectStatement, tableName, fieldNames);
    if (wherefieldNames.count() > 0 && !stmt.isEmpty())
    {
        stmt.append(" ");
        stmt.append(sqlStatement(WhereStatement, "", wherefieldNames));
    }
    if (!orderBySql.isEmpty())
    {
        stmt.append(" Order By ");
        stmt.append(orderBySql);
    }
    return stmt;
}

QString DMSDbSession::selectSqlStatement(const QString &tableName, const QStringList &fieldNames,
    const QString &whereSql, const QString &orderBySql /*= QString()*/) const
{
    QString stmt = sqlStatement(SelectStatement, tableName, fieldNames);
    if (!whereSql.isEmpty())
    {
        stmt.append(" Where ");
        stmt.append(whereSql);
    }
    if (!orderBySql.isEmpty())
    {
        stmt.append(" Order By ");
        stmt.append(orderBySql);
    }
    return stmt;
}

QString DMSDbSession::insertSqlStatement(const QString & tableName, const QStringList& valueFieldNames) const
{
    return sqlStatement(InsertStatement, tableName, valueFieldNames);
}

QString DMSDbSession::deleteSqlStatement(const QString & tableName, const QStringList& wherefieldNames) const
{
    QString stmt = sqlStatement(DeleteStatement, tableName, {});
    if (wherefieldNames.count() > 0 && !stmt.isEmpty())
    {
        stmt.append(" ");
        stmt.append(sqlStatement(WhereStatement, "", wherefieldNames));
    }
    return stmt;
}

QString DMSDbSession::updateSqlStatement(const QString & tableName, const QStringList& valuefieldNames,
    const QStringList& wherefieldNames) const
{
    QString stmt = sqlStatement(UpdateStatement, tableName, valuefieldNames);
    if (wherefieldNames.count() > 0 && !stmt.isEmpty())
    {
        stmt.append(" ");
        stmt.append(sqlStatement(WhereStatement, "", wherefieldNames));
    }
    return stmt;
}

bool DMSDbSession::execSQL(QSqlQuery &query, const QString &stmt, std::function<void()> prepareValues, bool prepStatement)
{
    if (stmt.isEmpty())
        return false;

    if (prepStatement)
    {
        if (query.lastQuery() != stmt)
        {
            if (!query.prepare(stmt))
            {
                error = query.lastError();
                qDebug() << error;
                return false;
            }
        }
        prepareValues();
        if (m_isOutputSql)
        {
            qDebug() << stmt;
#ifdef TEST
            QMap<QString, QVariant> boundValues = query.boundValues();
            for (auto it = boundValues.begin(); it != boundValues.end(); ++it)
            {
                qDebug() << it.key() << "=" << it.value();
            }
#endif // TEST
        }
        if (!query.exec()) {
            error = query.lastError();
            qDebug() << error;
            return false;
        }
    }
    else
    {
        if (!query.exec(stmt)) {
            error = query.lastError();
            qDebug() << error;
            return false;
        }
    }
    return true;
}

bool DMSDbSession::execSQL(QSqlQuery &query, const QString &stmt)
{
    return execSQL(query, stmt, []() {}, false);
}

bool DMSDbSession::queryData(QSqlQuery &query, const QString &tableName, const QStringList &fieldNames,
    const QStringList &whereFields, const QVector<QVariant> &bindValues, const QString &orderBySql)
{
    QString stmt = selectSqlStatement(tableName, fieldNames, whereFields, orderBySql);
    bool Result = execSQL(query, stmt,
        [&]() {
        for (auto vValue : bindValues)
            query.addBindValue(vValue);
    });
    return Result;
}

bool DMSDbSession::queryData(QSqlQuery &query, const QString &tableName, const QString &orderBySql)
{
    return queryData(query, tableName, {}, {}, {}, orderBySql);
}

int DMSDbSession::queryMaxValue(const QString &tableName, const QString &fieldName)
{
    QSqlQuery query(m_db);
    QString stmt = QString("SELECT MAX(%1) FROM %2").arg(fieldName).arg(tableName);
    if (execSQL(query, stmt) && query.next())
    {
        if (!query.value(0).isNull())
            return query.value(0).toInt();
    }
    return -1;
}

bool DMSDbSession::insertData(QSqlQuery &query, const QString &tableName, const QStringList &fieldNames,
    const QVector<QVariant> &bindValues)
{
    QString stmt = insertSqlStatement(tableName, fieldNames);
    bool Result = execSQL(query, stmt,
        [&]() {
        for (auto vValue : bindValues)
            query.addBindValue(vValue);
    });
    if (m_isOutputSql && Result)
        qDebug() << "lastInsertId:" << query.lastInsertId();
    return Result;
}

bool DMSDbSession::deleteData(QSqlQuery &query, const QString &tableName, const QStringList &whereFields,
    const QVector<QVariant> &bindValues)
{
    QString stmt = deleteSqlStatement(tableName, whereFields);
    bool Result = execSQL(query, stmt,
        [&]() {
        for (auto vValue : bindValues)
            query.addBindValue(vValue);
    }, whereFields.count() > 0);
    return Result;
}

bool DMSDbSession::updateData(QSqlQuery &query, const QString &tableName, const QStringList &fieldNames,
    const QStringList &whereFields, const QVector<QVariant> &bindValues)
{
    QString stmt = updateSqlStatement(tableName, fieldNames, whereFields);
    bool Result = execSQL(query, stmt,
        [&]() {
        for (auto vValue : bindValues)
            query.addBindValue(vValue);
    });
    return Result;
}

bool DMSDbSession::saveData(QSqlQuery &query, bool isAppend, const QString &tableName, const QStringList &fieldNames,
    const QStringList &whereFields, const QVector<QVariant> &bindValues)
{
    if (isAppend)
    {
        return insertData(query, tableName, fieldNames, bindValues);
    }
    else
    {
        return updateData(query, tableName, fieldNames, whereFields, bindValues);
    }
}

void DMSDbSession::importData(QSqlQuery &sourceQuery, const QStringList &sourceFields,
    const QString &targetTable, const QStringList &targetFields,
    BeforeInsertFunc onBeforeInsert, AfterInsertFunc onAfterInsert)
{
    QSqlQuery query(database());
    int nRecNo = 0;
    while (sourceQuery.next())
    {
        QVector<QVariant> fieldValues;
        for (int i = 0; i < targetFields.size(); ++i)
        {
            if (sourceFields[i] == c_sField_RecNo) // 取记录顺序号
                fieldValues << nRecNo;
            else if (sourceFields[i].isEmpty())
                fieldValues << QVariant();
            else
                fieldValues << sourceQuery.value(sourceFields[i]);
        }
        if (onBeforeInsert)
            onBeforeInsert(targetFields, fieldValues);
        if (insertData(query, targetTable, targetFields, fieldValues))
        {
            if (onAfterInsert)
                onAfterInsert(sourceQuery, query);
            ++nRecNo;
        }
    }
}

void DMSDbSession::importData(QSqlQuery &sourceQuery, const QString &targetTable, const QStringList &exclueFields,
    BeforeInsertFunc onBeforeInsert, AfterInsertFunc onAfterInsert)
{
    if (!sourceQuery.isActive())
        return;
    QSqlRecord record = sourceQuery.record();
    QStringList sourceFields;
    for (int i = 0; i < record.count(); ++i)
    {
        if (exclueFields.contains(record.fieldName(i), Qt::CaseInsensitive))
            continue;
        sourceFields << record.fieldName(i);
    }
    importData(sourceQuery, sourceFields, targetTable, sourceFields, onBeforeInsert, onAfterInsert);
}
