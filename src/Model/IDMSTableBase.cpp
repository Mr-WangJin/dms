#include "stdafx.h"
#include "IDMSTableBase.h"

IDMSTableBase::~IDMSTableBase()
{

}

DMSTableBase::DMSTableBase()
{
}

DMSTableBase::~DMSTableBase()
{

}

int DMSTableBase::id() const
{
    return m_id;
}

void DMSTableBase::setID(int id)
{
    m_id = id;
}
