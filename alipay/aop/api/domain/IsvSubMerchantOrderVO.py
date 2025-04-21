#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IsvSubMerchantOrderVO(object):

    def __init__(self):
        self._m_order_id = None
        self._sub_order_status = None
        self._sub_order_type = None

    @property
    def m_order_id(self):
        return self._m_order_id

    @m_order_id.setter
    def m_order_id(self, value):
        self._m_order_id = value
    @property
    def sub_order_status(self):
        return self._sub_order_status

    @sub_order_status.setter
    def sub_order_status(self, value):
        self._sub_order_status = value
    @property
    def sub_order_type(self):
        return self._sub_order_type

    @sub_order_type.setter
    def sub_order_type(self, value):
        self._sub_order_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.m_order_id:
            if hasattr(self.m_order_id, 'to_alipay_dict'):
                params['m_order_id'] = self.m_order_id.to_alipay_dict()
            else:
                params['m_order_id'] = self.m_order_id
        if self.sub_order_status:
            if hasattr(self.sub_order_status, 'to_alipay_dict'):
                params['sub_order_status'] = self.sub_order_status.to_alipay_dict()
            else:
                params['sub_order_status'] = self.sub_order_status
        if self.sub_order_type:
            if hasattr(self.sub_order_type, 'to_alipay_dict'):
                params['sub_order_type'] = self.sub_order_type.to_alipay_dict()
            else:
                params['sub_order_type'] = self.sub_order_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IsvSubMerchantOrderVO()
        if 'm_order_id' in d:
            o.m_order_id = d['m_order_id']
        if 'sub_order_status' in d:
            o.sub_order_status = d['sub_order_status']
        if 'sub_order_type' in d:
            o.sub_order_type = d['sub_order_type']
        return o


