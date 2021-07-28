#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataIotdataSearchlibraryBaiQueryModel(object):

    def __init__(self):
        self._account_id = None
        self._biz_id = None
        self._company_id = None
        self._content_id = None
        self._entity_data = None
        self._entity_desc = None
        self._entity_hash = None
        self._entity_type = None
        self._entity_url = None
        self._entity_vector = None
        self._ex_1 = None
        self._ex_2 = None
        self._ex_3 = None
        self._ex_4 = None
        self._ex_5 = None
        self._time_stamp = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, value):
        self._company_id = value
    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def entity_data(self):
        return self._entity_data

    @entity_data.setter
    def entity_data(self, value):
        self._entity_data = value
    @property
    def entity_desc(self):
        return self._entity_desc

    @entity_desc.setter
    def entity_desc(self, value):
        self._entity_desc = value
    @property
    def entity_hash(self):
        return self._entity_hash

    @entity_hash.setter
    def entity_hash(self, value):
        self._entity_hash = value
    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        self._entity_type = value
    @property
    def entity_url(self):
        return self._entity_url

    @entity_url.setter
    def entity_url(self, value):
        self._entity_url = value
    @property
    def entity_vector(self):
        return self._entity_vector

    @entity_vector.setter
    def entity_vector(self, value):
        self._entity_vector = value
    @property
    def ex_1(self):
        return self._ex_1

    @ex_1.setter
    def ex_1(self, value):
        self._ex_1 = value
    @property
    def ex_2(self):
        return self._ex_2

    @ex_2.setter
    def ex_2(self, value):
        self._ex_2 = value
    @property
    def ex_3(self):
        return self._ex_3

    @ex_3.setter
    def ex_3(self, value):
        self._ex_3 = value
    @property
    def ex_4(self):
        return self._ex_4

    @ex_4.setter
    def ex_4(self, value):
        self._ex_4 = value
    @property
    def ex_5(self):
        return self._ex_5

    @ex_5.setter
    def ex_5(self, value):
        self._ex_5 = value
    @property
    def time_stamp(self):
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, value):
        self._time_stamp = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.company_id:
            if hasattr(self.company_id, 'to_alipay_dict'):
                params['company_id'] = self.company_id.to_alipay_dict()
            else:
                params['company_id'] = self.company_id
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.entity_data:
            if hasattr(self.entity_data, 'to_alipay_dict'):
                params['entity_data'] = self.entity_data.to_alipay_dict()
            else:
                params['entity_data'] = self.entity_data
        if self.entity_desc:
            if hasattr(self.entity_desc, 'to_alipay_dict'):
                params['entity_desc'] = self.entity_desc.to_alipay_dict()
            else:
                params['entity_desc'] = self.entity_desc
        if self.entity_hash:
            if hasattr(self.entity_hash, 'to_alipay_dict'):
                params['entity_hash'] = self.entity_hash.to_alipay_dict()
            else:
                params['entity_hash'] = self.entity_hash
        if self.entity_type:
            if hasattr(self.entity_type, 'to_alipay_dict'):
                params['entity_type'] = self.entity_type.to_alipay_dict()
            else:
                params['entity_type'] = self.entity_type
        if self.entity_url:
            if hasattr(self.entity_url, 'to_alipay_dict'):
                params['entity_url'] = self.entity_url.to_alipay_dict()
            else:
                params['entity_url'] = self.entity_url
        if self.entity_vector:
            if hasattr(self.entity_vector, 'to_alipay_dict'):
                params['entity_vector'] = self.entity_vector.to_alipay_dict()
            else:
                params['entity_vector'] = self.entity_vector
        if self.ex_1:
            if hasattr(self.ex_1, 'to_alipay_dict'):
                params['ex_1'] = self.ex_1.to_alipay_dict()
            else:
                params['ex_1'] = self.ex_1
        if self.ex_2:
            if hasattr(self.ex_2, 'to_alipay_dict'):
                params['ex_2'] = self.ex_2.to_alipay_dict()
            else:
                params['ex_2'] = self.ex_2
        if self.ex_3:
            if hasattr(self.ex_3, 'to_alipay_dict'):
                params['ex_3'] = self.ex_3.to_alipay_dict()
            else:
                params['ex_3'] = self.ex_3
        if self.ex_4:
            if hasattr(self.ex_4, 'to_alipay_dict'):
                params['ex_4'] = self.ex_4.to_alipay_dict()
            else:
                params['ex_4'] = self.ex_4
        if self.ex_5:
            if hasattr(self.ex_5, 'to_alipay_dict'):
                params['ex_5'] = self.ex_5.to_alipay_dict()
            else:
                params['ex_5'] = self.ex_5
        if self.time_stamp:
            if hasattr(self.time_stamp, 'to_alipay_dict'):
                params['time_stamp'] = self.time_stamp.to_alipay_dict()
            else:
                params['time_stamp'] = self.time_stamp
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataIotdataSearchlibraryBaiQueryModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'company_id' in d:
            o.company_id = d['company_id']
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'entity_data' in d:
            o.entity_data = d['entity_data']
        if 'entity_desc' in d:
            o.entity_desc = d['entity_desc']
        if 'entity_hash' in d:
            o.entity_hash = d['entity_hash']
        if 'entity_type' in d:
            o.entity_type = d['entity_type']
        if 'entity_url' in d:
            o.entity_url = d['entity_url']
        if 'entity_vector' in d:
            o.entity_vector = d['entity_vector']
        if 'ex_1' in d:
            o.ex_1 = d['ex_1']
        if 'ex_2' in d:
            o.ex_2 = d['ex_2']
        if 'ex_3' in d:
            o.ex_3 = d['ex_3']
        if 'ex_4' in d:
            o.ex_4 = d['ex_4']
        if 'ex_5' in d:
            o.ex_5 = d['ex_5']
        if 'time_stamp' in d:
            o.time_stamp = d['time_stamp']
        return o


