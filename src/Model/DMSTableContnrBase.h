#pragma once

//所有表的容器类接口
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

