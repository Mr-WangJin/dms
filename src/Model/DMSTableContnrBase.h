#pragma once

//���б��������ӿ�
class IDMSTableContnr
{
public:
    virtual ~IDMSTableContnr() {};
};



class DMSTableContner : public IDMSTableContnr
{
public:
    DMSTableContner();
    virtual ~DMSTableContner();
};

