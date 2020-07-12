#pragma once
/*!
* @file     DMSSession.h
* @brief    数据库会话对象实现单元
*/

class DMSDbSession
{
public:
    enum DatabaseType {
        SQLite, // SQLite数据库
        Access  // Access数据库
    };
    enum StatementType {
        WhereStatement, SelectStatement,
        InsertStatement, DeleteStatement, UpdateStatement
    };
    typedef std::function<void(const QStringList &, QVector<QVariant> &)> BeforeInsertFunc;
    typedef std::function<void(QSqlQuery&, QSqlQuery&)> AfterInsertFunc;

public:
    DMSDbSession(const QString &fileName, DatabaseType dbType = SQLite);
    ~DMSDbSession();
    virtual QString fileName();
    void setIsOutputSql(bool val);

    QSqlDatabase database() const;

    QSqlError lastError() const;

    bool open();
    
    void close();
    
    bool transaction();
    
    bool commit();
    
    bool rollback();
   
    void close_foreignKeys();
   
    void open_foreignKeys();
    
    QString sqlStatement(StatementType type, const QString &tableName, const QStringList &fieldNames) const;
    
    QString selectSqlStatement(const QString &tableName, const QStringList &fieldNames,
        const QStringList &wherefieldNames = {}, const QString &orderBySql = QString()) const;
   
    QString selectSqlStatement(const QString &tableName, const QStringList &fieldNames,
        const QString &whereSql, const QString &orderBySql = QString()) const;
    
    QString insertSqlStatement(const QString &tableName, const QStringList &valueFieldNames) const;
    
    QString deleteSqlStatement(const QString &tableName, const QStringList &wherefieldNames) const;
    
    QString updateSqlStatement(const QString &tableName, const QStringList &valuefieldNames,
        const QStringList &wherefieldNames) const;
    
    bool execSQL(QSqlQuery &query, const QString &stmt, std::function<void()> prepareValues, bool prepStatement = true);
    bool execSQL(QSqlQuery &query, const QString &stmt);
    /**
    * @brief  查询数据
    * @param orderBySql: 格式 "Id Desc" 或 "OrderNum"
    */
    bool queryData(QSqlQuery &query, const QString &tableName, const QStringList &fieldNames,
        const QStringList &whereFields, const QVector<QVariant> &bindValues, const QString &orderBySql = QString());
    
    bool queryData(QSqlQuery &query, const QString &tableName, const QString &orderBySql = QString());
   
    int queryMaxValue(const QString &tableName, const QString &fieldName);
   
    bool insertData(QSqlQuery &query, const QString &tableName, const QStringList &fieldNames,
        const QVector<QVariant> &bindValues);
    
    bool deleteData(QSqlQuery &query, const QString &tableName, const QStringList &whereFields,
        const QVector<QVariant> &bindValues);
    
    bool updateData(QSqlQuery &query, const QString &tableName, const QStringList &fieldNames,
        const QStringList &whereFields, const QVector<QVariant> &bindValues);
   
    bool saveData(QSqlQuery &query, bool isAppend, const QString &tableName, const QStringList &fieldNames,
        const QStringList &whereFields, const QVector<QVariant> &bindValues);
    
    void importData(QSqlQuery &sourceQuery, const QStringList &sourceFields,
        const QString &targetTable, const QStringList &targetFields,
        BeforeInsertFunc onBeforeInsert, AfterInsertFunc onAfterInsert);
    
    void importData(QSqlQuery &sourceQuery, const QString &targetTable, const QStringList &exclueFields,
        BeforeInsertFunc onBeforeInsert, AfterInsertFunc onAfterInsert);
protected:
    DatabaseType m_dbType;  //数据库类型
    QString m_sFileName;    //
    QSqlDatabase m_db;
    QSqlError error;
    bool m_isOutputSql{ false };
};

