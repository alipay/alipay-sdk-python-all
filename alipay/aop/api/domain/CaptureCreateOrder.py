#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MapParameter import MapParameter
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MapParameter import MapParameter


class CaptureCreateOrder(object):

    def __init__(self):
        self._ar_no = None
        self._ar_source = None
        self._business_recognize_ext = None
        self._capture_amount = None
        self._capture_date = None
        self._ext_info = None
        self._inst_id = None
        self._ip_id = None
        self._ip_role_id = None
        self._out_biz_no = None
        self._pd_code = None
        self._pd_source = None
        self._source = None
        self._user_source = None

    @property
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value
    @property
    def ar_source(self):
        return self._ar_source

    @ar_source.setter
    def ar_source(self, value):
        self._ar_source = value
    @property
    def business_recognize_ext(self):
        return self._business_recognize_ext

    @business_recognize_ext.setter
    def business_recognize_ext(self, value):
        if isinstance(value, MapParameter):
            self._business_recognize_ext = value
        else:
            self._business_recognize_ext = MapParameter.from_alipay_dict(value)
    @property
    def capture_amount(self):
        return self._capture_amount

    @capture_amount.setter
    def capture_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._capture_amount = value
        else:
            self._capture_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def capture_date(self):
        return self._capture_date

    @capture_date.setter
    def capture_date(self, value):
        self._capture_date = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, MapParameter):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(MapParameter.from_alipay_dict(i))
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pd_code(self):
        return self._pd_code

    @pd_code.setter
    def pd_code(self, value):
        self._pd_code = value
    @property
    def pd_source(self):
        return self._pd_source

    @pd_source.setter
    def pd_source(self, value):
        self._pd_source = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_source(self):
        return self._user_source

    @user_source.setter
    def user_source(self, value):
        self._user_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.ar_no:
            if hasattr(self.ar_no, 'to_alipay_dict'):
                params['ar_no'] = self.ar_no.to_alipay_dict()
            else:
                params['ar_no'] = self.ar_no
        if self.ar_source:
            if hasattr(self.ar_source, 'to_alipay_dict'):
                params['ar_source'] = self.ar_source.to_alipay_dict()
            else:
                params['ar_source'] = self.ar_source
        if self.business_recognize_ext:
            if hasattr(self.business_recognize_ext, 'to_alipay_dict'):
                params['business_recognize_ext'] = self.business_recognize_ext.to_alipay_dict()
            else:
                params['business_recognize_ext'] = self.business_recognize_ext
        if self.capture_amount:
            if hasattr(self.capture_amount, 'to_alipay_dict'):
                params['capture_amount'] = self.capture_amount.to_alipay_dict()
            else:
                params['capture_amount'] = self.capture_amount
        if self.capture_date:
            if hasattr(self.capture_date, 'to_alipay_dict'):
                params['capture_date'] = self.capture_date.to_alipay_dict()
            else:
                params['capture_date'] = self.capture_date
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.pd_code:
            if hasattr(self.pd_code, 'to_alipay_dict'):
                params['pd_code'] = self.pd_code.to_alipay_dict()
            else:
                params['pd_code'] = self.pd_code
        if self.pd_source:
            if hasattr(self.pd_source, 'to_alipay_dict'):
                params['pd_source'] = self.pd_source.to_alipay_dict()
            else:
                params['pd_source'] = self.pd_source
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.user_source:
            if hasattr(self.user_source, 'to_alipay_dict'):
                params['user_source'] = self.user_source.to_alipay_dict()
            else:
                params['user_source'] = self.user_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CaptureCreateOrder()
        if 'ar_no' in d:
            o.ar_no = d['ar_no']
        if 'ar_source' in d:
            o.ar_source = d['ar_source']
        if 'business_recognize_ext' in d:
            o.business_recognize_ext = d['business_recognize_ext']
        if 'capture_amount' in d:
            o.capture_amount = d['capture_amount']
        if 'capture_date' in d:
            o.capture_date = d['capture_date']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pd_code' in d:
            o.pd_code = d['pd_code']
        if 'pd_source' in d:
            o.pd_source = d['pd_source']
        if 'source' in d:
            o.source = d['source']
        if 'user_source' in d:
            o.user_source = d['user_source']
        return o


