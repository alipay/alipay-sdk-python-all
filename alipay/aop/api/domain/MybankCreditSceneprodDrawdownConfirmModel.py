#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SceneDrawdownDetail import SceneDrawdownDetail


class MybankCreditSceneprodDrawdownConfirmModel(object):

    def __init__(self):
        self._apply_no = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._drawdown_list = None
        self._error_msg = None
        self._fin_order_no = None
        self._process_result = None
        self._remark = None
        self._request_id = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def drawdown_list(self):
        return self._drawdown_list

    @drawdown_list.setter
    def drawdown_list(self, value):
        if isinstance(value, list):
            self._drawdown_list = list()
            for i in value:
                if isinstance(i, SceneDrawdownDetail):
                    self._drawdown_list.append(i)
                else:
                    self._drawdown_list.append(SceneDrawdownDetail.from_alipay_dict(i))
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def fin_order_no(self):
        return self._fin_order_no

    @fin_order_no.setter
    def fin_order_no(self, value):
        self._fin_order_no = value
    @property
    def process_result(self):
        return self._process_result

    @process_result.setter
    def process_result(self, value):
        self._process_result = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.drawdown_list:
            if isinstance(self.drawdown_list, list):
                for i in range(0, len(self.drawdown_list)):
                    element = self.drawdown_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.drawdown_list[i] = element.to_alipay_dict()
            if hasattr(self.drawdown_list, 'to_alipay_dict'):
                params['drawdown_list'] = self.drawdown_list.to_alipay_dict()
            else:
                params['drawdown_list'] = self.drawdown_list
        if self.error_msg:
            if hasattr(self.error_msg, 'to_alipay_dict'):
                params['error_msg'] = self.error_msg.to_alipay_dict()
            else:
                params['error_msg'] = self.error_msg
        if self.fin_order_no:
            if hasattr(self.fin_order_no, 'to_alipay_dict'):
                params['fin_order_no'] = self.fin_order_no.to_alipay_dict()
            else:
                params['fin_order_no'] = self.fin_order_no
        if self.process_result:
            if hasattr(self.process_result, 'to_alipay_dict'):
                params['process_result'] = self.process_result.to_alipay_dict()
            else:
                params['process_result'] = self.process_result
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSceneprodDrawdownConfirmModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'drawdown_list' in d:
            o.drawdown_list = d['drawdown_list']
        if 'error_msg' in d:
            o.error_msg = d['error_msg']
        if 'fin_order_no' in d:
            o.fin_order_no = d['fin_order_no']
        if 'process_result' in d:
            o.process_result = d['process_result']
        if 'remark' in d:
            o.remark = d['remark']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


