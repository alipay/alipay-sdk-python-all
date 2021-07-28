#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataservicePropertyBusinesspropertyCreateModel(object):

    def __init__(self):
        self._biz_owner_id = None
        self._business_profile_category_id = None
        self._business_profile_id = None
        self._column_name = None
        self._column_type = None
        self._creator_id = None
        self._data_owner_id = None
        self._data_type = None
        self._enum_id = None
        self._personality_info = None
        self._physical_type = None
        self._primary_key = None
        self._proc_type = None
        self._property_desc = None
        self._propery_name = None
        self._quality_owner_id = None
        self._source_channel = None
        self._table_guid = None

    @property
    def biz_owner_id(self):
        return self._biz_owner_id

    @biz_owner_id.setter
    def biz_owner_id(self, value):
        self._biz_owner_id = value
    @property
    def business_profile_category_id(self):
        return self._business_profile_category_id

    @business_profile_category_id.setter
    def business_profile_category_id(self, value):
        self._business_profile_category_id = value
    @property
    def business_profile_id(self):
        return self._business_profile_id

    @business_profile_id.setter
    def business_profile_id(self, value):
        self._business_profile_id = value
    @property
    def column_name(self):
        return self._column_name

    @column_name.setter
    def column_name(self, value):
        self._column_name = value
    @property
    def column_type(self):
        return self._column_type

    @column_type.setter
    def column_type(self, value):
        self._column_type = value
    @property
    def creator_id(self):
        return self._creator_id

    @creator_id.setter
    def creator_id(self, value):
        self._creator_id = value
    @property
    def data_owner_id(self):
        return self._data_owner_id

    @data_owner_id.setter
    def data_owner_id(self, value):
        self._data_owner_id = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def enum_id(self):
        return self._enum_id

    @enum_id.setter
    def enum_id(self, value):
        self._enum_id = value
    @property
    def personality_info(self):
        return self._personality_info

    @personality_info.setter
    def personality_info(self, value):
        if isinstance(value, list):
            self._personality_info = list()
            for i in value:
                self._personality_info.append(i)
    @property
    def physical_type(self):
        return self._physical_type

    @physical_type.setter
    def physical_type(self, value):
        self._physical_type = value
    @property
    def primary_key(self):
        return self._primary_key

    @primary_key.setter
    def primary_key(self, value):
        self._primary_key = value
    @property
    def proc_type(self):
        return self._proc_type

    @proc_type.setter
    def proc_type(self, value):
        self._proc_type = value
    @property
    def property_desc(self):
        return self._property_desc

    @property_desc.setter
    def property_desc(self, value):
        self._property_desc = value
    @property
    def propery_name(self):
        return self._propery_name

    @propery_name.setter
    def propery_name(self, value):
        self._propery_name = value
    @property
    def quality_owner_id(self):
        return self._quality_owner_id

    @quality_owner_id.setter
    def quality_owner_id(self, value):
        self._quality_owner_id = value
    @property
    def source_channel(self):
        return self._source_channel

    @source_channel.setter
    def source_channel(self, value):
        self._source_channel = value
    @property
    def table_guid(self):
        return self._table_guid

    @table_guid.setter
    def table_guid(self, value):
        self._table_guid = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_owner_id:
            if hasattr(self.biz_owner_id, 'to_alipay_dict'):
                params['biz_owner_id'] = self.biz_owner_id.to_alipay_dict()
            else:
                params['biz_owner_id'] = self.biz_owner_id
        if self.business_profile_category_id:
            if hasattr(self.business_profile_category_id, 'to_alipay_dict'):
                params['business_profile_category_id'] = self.business_profile_category_id.to_alipay_dict()
            else:
                params['business_profile_category_id'] = self.business_profile_category_id
        if self.business_profile_id:
            if hasattr(self.business_profile_id, 'to_alipay_dict'):
                params['business_profile_id'] = self.business_profile_id.to_alipay_dict()
            else:
                params['business_profile_id'] = self.business_profile_id
        if self.column_name:
            if hasattr(self.column_name, 'to_alipay_dict'):
                params['column_name'] = self.column_name.to_alipay_dict()
            else:
                params['column_name'] = self.column_name
        if self.column_type:
            if hasattr(self.column_type, 'to_alipay_dict'):
                params['column_type'] = self.column_type.to_alipay_dict()
            else:
                params['column_type'] = self.column_type
        if self.creator_id:
            if hasattr(self.creator_id, 'to_alipay_dict'):
                params['creator_id'] = self.creator_id.to_alipay_dict()
            else:
                params['creator_id'] = self.creator_id
        if self.data_owner_id:
            if hasattr(self.data_owner_id, 'to_alipay_dict'):
                params['data_owner_id'] = self.data_owner_id.to_alipay_dict()
            else:
                params['data_owner_id'] = self.data_owner_id
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.enum_id:
            if hasattr(self.enum_id, 'to_alipay_dict'):
                params['enum_id'] = self.enum_id.to_alipay_dict()
            else:
                params['enum_id'] = self.enum_id
        if self.personality_info:
            if isinstance(self.personality_info, list):
                for i in range(0, len(self.personality_info)):
                    element = self.personality_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.personality_info[i] = element.to_alipay_dict()
            if hasattr(self.personality_info, 'to_alipay_dict'):
                params['personality_info'] = self.personality_info.to_alipay_dict()
            else:
                params['personality_info'] = self.personality_info
        if self.physical_type:
            if hasattr(self.physical_type, 'to_alipay_dict'):
                params['physical_type'] = self.physical_type.to_alipay_dict()
            else:
                params['physical_type'] = self.physical_type
        if self.primary_key:
            if hasattr(self.primary_key, 'to_alipay_dict'):
                params['primary_key'] = self.primary_key.to_alipay_dict()
            else:
                params['primary_key'] = self.primary_key
        if self.proc_type:
            if hasattr(self.proc_type, 'to_alipay_dict'):
                params['proc_type'] = self.proc_type.to_alipay_dict()
            else:
                params['proc_type'] = self.proc_type
        if self.property_desc:
            if hasattr(self.property_desc, 'to_alipay_dict'):
                params['property_desc'] = self.property_desc.to_alipay_dict()
            else:
                params['property_desc'] = self.property_desc
        if self.propery_name:
            if hasattr(self.propery_name, 'to_alipay_dict'):
                params['propery_name'] = self.propery_name.to_alipay_dict()
            else:
                params['propery_name'] = self.propery_name
        if self.quality_owner_id:
            if hasattr(self.quality_owner_id, 'to_alipay_dict'):
                params['quality_owner_id'] = self.quality_owner_id.to_alipay_dict()
            else:
                params['quality_owner_id'] = self.quality_owner_id
        if self.source_channel:
            if hasattr(self.source_channel, 'to_alipay_dict'):
                params['source_channel'] = self.source_channel.to_alipay_dict()
            else:
                params['source_channel'] = self.source_channel
        if self.table_guid:
            if hasattr(self.table_guid, 'to_alipay_dict'):
                params['table_guid'] = self.table_guid.to_alipay_dict()
            else:
                params['table_guid'] = self.table_guid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataservicePropertyBusinesspropertyCreateModel()
        if 'biz_owner_id' in d:
            o.biz_owner_id = d['biz_owner_id']
        if 'business_profile_category_id' in d:
            o.business_profile_category_id = d['business_profile_category_id']
        if 'business_profile_id' in d:
            o.business_profile_id = d['business_profile_id']
        if 'column_name' in d:
            o.column_name = d['column_name']
        if 'column_type' in d:
            o.column_type = d['column_type']
        if 'creator_id' in d:
            o.creator_id = d['creator_id']
        if 'data_owner_id' in d:
            o.data_owner_id = d['data_owner_id']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'enum_id' in d:
            o.enum_id = d['enum_id']
        if 'personality_info' in d:
            o.personality_info = d['personality_info']
        if 'physical_type' in d:
            o.physical_type = d['physical_type']
        if 'primary_key' in d:
            o.primary_key = d['primary_key']
        if 'proc_type' in d:
            o.proc_type = d['proc_type']
        if 'property_desc' in d:
            o.property_desc = d['property_desc']
        if 'propery_name' in d:
            o.propery_name = d['propery_name']
        if 'quality_owner_id' in d:
            o.quality_owner_id = d['quality_owner_id']
        if 'source_channel' in d:
            o.source_channel = d['source_channel']
        if 'table_guid' in d:
            o.table_guid = d['table_guid']
        return o


