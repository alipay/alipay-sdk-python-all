#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PersonalityInfoDTO import PersonalityInfoDTO


class BusinessPropertyDTO(object):

    def __init__(self):
        self._biz_owner_id = None
        self._business_profile_id = None
        self._business_property_id = None
        self._column_name = None
        self._column_type = None
        self._creator_id = None
        self._data_owner_id = None
        self._english_name = None
        self._personality_info = None
        self._property_desc = None
        self._propery_name = None
        self._quality_owner_id = None
        self._stauts = None
        self._table_guid = None

    @property
    def biz_owner_id(self):
        return self._biz_owner_id

    @biz_owner_id.setter
    def biz_owner_id(self, value):
        self._biz_owner_id = value
    @property
    def business_profile_id(self):
        return self._business_profile_id

    @business_profile_id.setter
    def business_profile_id(self, value):
        self._business_profile_id = value
    @property
    def business_property_id(self):
        return self._business_property_id

    @business_property_id.setter
    def business_property_id(self, value):
        self._business_property_id = value
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
    def english_name(self):
        return self._english_name

    @english_name.setter
    def english_name(self, value):
        self._english_name = value
    @property
    def personality_info(self):
        return self._personality_info

    @personality_info.setter
    def personality_info(self, value):
        if isinstance(value, list):
            self._personality_info = list()
            for i in value:
                if isinstance(i, PersonalityInfoDTO):
                    self._personality_info.append(i)
                else:
                    self._personality_info.append(PersonalityInfoDTO.from_alipay_dict(i))
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
    def stauts(self):
        return self._stauts

    @stauts.setter
    def stauts(self, value):
        self._stauts = value
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
        if self.business_profile_id:
            if hasattr(self.business_profile_id, 'to_alipay_dict'):
                params['business_profile_id'] = self.business_profile_id.to_alipay_dict()
            else:
                params['business_profile_id'] = self.business_profile_id
        if self.business_property_id:
            if hasattr(self.business_property_id, 'to_alipay_dict'):
                params['business_property_id'] = self.business_property_id.to_alipay_dict()
            else:
                params['business_property_id'] = self.business_property_id
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
        if self.english_name:
            if hasattr(self.english_name, 'to_alipay_dict'):
                params['english_name'] = self.english_name.to_alipay_dict()
            else:
                params['english_name'] = self.english_name
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
        if self.stauts:
            if hasattr(self.stauts, 'to_alipay_dict'):
                params['stauts'] = self.stauts.to_alipay_dict()
            else:
                params['stauts'] = self.stauts
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
        o = BusinessPropertyDTO()
        if 'biz_owner_id' in d:
            o.biz_owner_id = d['biz_owner_id']
        if 'business_profile_id' in d:
            o.business_profile_id = d['business_profile_id']
        if 'business_property_id' in d:
            o.business_property_id = d['business_property_id']
        if 'column_name' in d:
            o.column_name = d['column_name']
        if 'column_type' in d:
            o.column_type = d['column_type']
        if 'creator_id' in d:
            o.creator_id = d['creator_id']
        if 'data_owner_id' in d:
            o.data_owner_id = d['data_owner_id']
        if 'english_name' in d:
            o.english_name = d['english_name']
        if 'personality_info' in d:
            o.personality_info = d['personality_info']
        if 'property_desc' in d:
            o.property_desc = d['property_desc']
        if 'propery_name' in d:
            o.propery_name = d['propery_name']
        if 'quality_owner_id' in d:
            o.quality_owner_id = d['quality_owner_id']
        if 'stauts' in d:
            o.stauts = d['stauts']
        if 'table_guid' in d:
            o.table_guid = d['table_guid']
        return o


