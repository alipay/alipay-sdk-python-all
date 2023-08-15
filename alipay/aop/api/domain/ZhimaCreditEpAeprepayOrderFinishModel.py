#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ZmEpAePrepayExtParam import ZmEpAePrepayExtParam


class ZhimaCreditEpAeprepayOrderFinishModel(object):

    def __init__(self):
        self._ext_param = None
        self._order_num = None
        self._order_time_millis = None
        self._seller_login_id = None

    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        if isinstance(value, ZmEpAePrepayExtParam):
            self._ext_param = value
        else:
            self._ext_param = ZmEpAePrepayExtParam.from_alipay_dict(value)
    @property
    def order_num(self):
        return self._order_num

    @order_num.setter
    def order_num(self, value):
        self._order_num = value
    @property
    def order_time_millis(self):
        return self._order_time_millis

    @order_time_millis.setter
    def order_time_millis(self, value):
        self._order_time_millis = value
    @property
    def seller_login_id(self):
        return self._seller_login_id

    @seller_login_id.setter
    def seller_login_id(self, value):
        self._seller_login_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.order_num:
            if hasattr(self.order_num, 'to_alipay_dict'):
                params['order_num'] = self.order_num.to_alipay_dict()
            else:
                params['order_num'] = self.order_num
        if self.order_time_millis:
            if hasattr(self.order_time_millis, 'to_alipay_dict'):
                params['order_time_millis'] = self.order_time_millis.to_alipay_dict()
            else:
                params['order_time_millis'] = self.order_time_millis
        if self.seller_login_id:
            if hasattr(self.seller_login_id, 'to_alipay_dict'):
                params['seller_login_id'] = self.seller_login_id.to_alipay_dict()
            else:
                params['seller_login_id'] = self.seller_login_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpAeprepayOrderFinishModel()
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'order_num' in d:
            o.order_num = d['order_num']
        if 'order_time_millis' in d:
            o.order_time_millis = d['order_time_millis']
        if 'seller_login_id' in d:
            o.seller_login_id = d['seller_login_id']
        return o


