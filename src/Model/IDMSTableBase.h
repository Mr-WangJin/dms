#pragma once
/**
* @brief : ��Ľӿ��࣬���б���Ҫ����DMSTableBase
*/

class IDMSTableContnr;

class IDMSTableBase
{
public:
    virtual ~IDMSTableBase();

    virtual IDMSTableContnr* contnr() const = 0;

    virtual void beginEdit() = 0;
    virtual void endEdit() = 0;


    virtual int id() const = 0;
    virtual void setID(int id) = 0;

};

class DMSTableBase : public IDMSTableBase
{
public:
    DMSTableBase();
    virtual ~DMSTableBase();


    virtual int id() const override;
    virtual void setID(int id) override;


private:
    bool m_Modified{ false };
    int m_id{ -1 };


};



