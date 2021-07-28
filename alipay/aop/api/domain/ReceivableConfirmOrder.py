#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MapParameter import MapParameter
from alipay.aop.api.domain.MapParameter import MapParameter
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class ReceivableConfirmOrder(object):

    def __init__(self):
        self._ar_no = None
        self._ar_source = None
        self._begin_date = None
        self._business_recognize_ext = None
        self._calc_factor = None
        self._calc_method = None
        self._calc_period = None
        self._confirm_model = None
        self._end_date = None
        self._ext_info = None
        self._gmt_service = None
        self._inst_id = None
        self._ip_id = None
        self._ip_role_id = None
        self._out_biz_no = None
        self._pd_code = None
        self._pd_event_code = None
        self._pd_source = None
        self._receivable_amount = None
        self._receivable_type = None
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
    def begin_date(self):
        return self._begin_date

    @begin_date.setter
    def begin_date(self, value):
        self._begin_date = value
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
    def calc_factor(self):
        return self._calc_factor

    @calc_factor.setter
    def calc_factor(self, value):
        self._calc_factor = value
    @property
    def calc_method(self):
        return self._calc_method

    @calc_method.setter
    def calc_method(self, value):
        self._calc_method = value
    @property
    def calc_period(self):
        return self._calc_period

    @calc_period.setter
    def calc_period(self, value):
        self._calc_period = value
    @property
    def confirm_model(self):
        return self._confirm_model

    @confirm_model.setter
    def confirm_model(self, value):
        self._confirm_model = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
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
    def gmt_service(self):
        return self._gmt_service

    @gmt_service.setter
    def gmt_service(self, value):
        self._gmt_service = value
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
    def pd_event_code(self):
        return self._pd_event_code

    @pd_event_code.setter
    def pd_event_code(self, value):
        self._pd_event_code = value
    @property
    def pd_source(self):
        return self._pd_source

    @pd_source.setter
    def pd_source(self, value):
        self._pd_source = value
    @property
    def receivable_amount(self):
        return self._receivable_amount

    @receivable_amount.setter
    def receivable_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._receivable_amount = value
        else:
            self._receivable_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def receivable_type(self):
        return self._receivable_type

    @receivable_type.setter
    def receivable_type(self, value):
        self._receivable_type = value
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
        if self.begin_date:
            if hasattr(self.begin_date, 'to_alipay_dict'):
                params['begin_date'] = self.begin_date.to_alipay_dict()
            else:
                params['begin_date'] = self.begin_date
        if self.business_recognize_ext:
            if hasattr(self.business_recognize_ext, 'to_alipay_dict'):
                params['business_recognize_ext'] = self.business_recognize_ext.to_alipay_dict()
            else:
                params['business_recognize_ext'] = self.business_recognize_ext
        if self.calc_factor:
            if hasattr(self.calc_factor, 'to_alipay_dict'):
                params['calc_factor'] = self.calc_factor.to_alipay_dict()
            else:
                params['calc_factor'] = self.calc_factor
        if self.calc_method:
            if hasattr(self.calc_method, 'to_alipay_dict'):
                params['calc_method'] = self.calc_method.to_alipay_dict()
            else:
                params['calc_method'] = self.calc_method
        if self.calc_period:
            if hasattr(self.calc_period, 'to_alipay_dict'):
                params['calc_period'] = self.calc_period.to_alipay_dict()
            else:
                params['calc_period'] = self.calc_period
        if self.confirm_model:
            if hasattr(self.confirm_model, 'to_alipay_dict'):
                params['confirm_model'] = self.confirm_model.to_alipay_dict()
            else:
                params['confirm_model'] = self.confirm_model
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
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
        if self.gmt_service:
            if hasattr(self.gmt_service, 'to_alipay_dict'):
                params['gmt_service'] = self.gmt_service.to_alipay_dict()
            else:
                params['gmt_service'] = self.gmt_service
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
        if self.pd_event_code:
            if hasattr(self.pd_event_code, 'to_alipay_dict'):
                params['pd_event_code'] = self.pd_event_code.to_alipay_dict()
            else:
                params['pd_event_code'] = self.pd_event_code
        if self.pd_source:
            if hasattr(self.pd_source, 'to_alipay_dict'):
                params['pd_source'] = self.pd_source.to_alipay_dict()
            else:
                params['pd_source'] = self.pd_source
        if self.receivable_amount:
            if hasattr(self.receivable_amount, 'to_alipay_dict'):
                params['receivable_amount'] = self.receivable_amount.to_alipay_dict()
            else:
                params['receivable_amount'] = self.receivable_amount
        if self.receivable_type:
            if hasattr(self.receivable_type, 'to_alipay_dict'):
                params['receivable_type'] = self.receivable_type.to_alipay_dict()
            else:
                params['receivable_type'] = self.receivable_type
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
        o = ReceivableConfirmOrder()
        if 'ar_no' in d:
            o.ar_no = d['ar_no']
        if 'ar_source' in d:
            o.ar_source = d['ar_source']
        if 'begin_date' in d:
            o.begin_date = d['begin_date']
        if 'business_recognize_ext' in d:
            o.business_recognize_ext = d['business_recognize_ext']
        if 'calc_factor' in d:
            o.calc_factor = d['calc_factor']
        if 'calc_method' in d:
            o.calc_method = d['calc_method']
        if 'calc_period' in d:
            o.calc_period = d['calc_period']
        if 'confirm_model' in d:
            o.confirm_model = d['confirm_model']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gmt_service' in d:
            o.gmt_service = d['gmt_service']
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
        if 'pd_event_code' in d:
            o.pd_event_code = d['pd_event_code']
        if 'pd_source' in d:
            o.pd_source = d['pd_source']
        if 'receivable_amount' in d:
            o.receivable_amount = d['receivable_amount']
        if 'receivable_type' in d:
            o.receivable_type = d['receivable_type']
        if 'source' in d:
            o.source = d['source']
        if 'user_source' in d:
            o.user_source = d['user_source']
        return o


