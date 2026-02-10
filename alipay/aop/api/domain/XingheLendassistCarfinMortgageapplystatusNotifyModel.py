#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CarfinPreMortgageInfo import CarfinPreMortgageInfo
from alipay.aop.api.domain.XhExpressPostInfo import XhExpressPostInfo


class XingheLendassistCarfinMortgageapplystatusNotifyModel(object):

    def __init__(self):
        self._jksxh = None
        self._mortgage_no = None
        self._out_mortgage_no = None
        self._pre_mortgage_info = None
        self._proxy_invalid_file_list = None
        self._receiver_info = None
        self._refuse_msg = None
        self._status = None
        self._supple_agreement_list = None
        self._supple_file_list = None

    @property
    def jksxh(self):
        return self._jksxh

    @jksxh.setter
    def jksxh(self, value):
        self._jksxh = value
    @property
    def mortgage_no(self):
        return self._mortgage_no

    @mortgage_no.setter
    def mortgage_no(self, value):
        self._mortgage_no = value
    @property
    def out_mortgage_no(self):
        return self._out_mortgage_no

    @out_mortgage_no.setter
    def out_mortgage_no(self, value):
        self._out_mortgage_no = value
    @property
    def pre_mortgage_info(self):
        return self._pre_mortgage_info

    @pre_mortgage_info.setter
    def pre_mortgage_info(self, value):
        if isinstance(value, CarfinPreMortgageInfo):
            self._pre_mortgage_info = value
        else:
            self._pre_mortgage_info = CarfinPreMortgageInfo.from_alipay_dict(value)
    @property
    def proxy_invalid_file_list(self):
        return self._proxy_invalid_file_list

    @proxy_invalid_file_list.setter
    def proxy_invalid_file_list(self, value):
        if isinstance(value, list):
            self._proxy_invalid_file_list = list()
            for i in value:
                self._proxy_invalid_file_list.append(i)
    @property
    def receiver_info(self):
        return self._receiver_info

    @receiver_info.setter
    def receiver_info(self, value):
        if isinstance(value, XhExpressPostInfo):
            self._receiver_info = value
        else:
            self._receiver_info = XhExpressPostInfo.from_alipay_dict(value)
    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        self._refuse_msg = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def supple_agreement_list(self):
        return self._supple_agreement_list

    @supple_agreement_list.setter
    def supple_agreement_list(self, value):
        if isinstance(value, list):
            self._supple_agreement_list = list()
            for i in value:
                self._supple_agreement_list.append(i)
    @property
    def supple_file_list(self):
        return self._supple_file_list

    @supple_file_list.setter
    def supple_file_list(self, value):
        if isinstance(value, list):
            self._supple_file_list = list()
            for i in value:
                self._supple_file_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.jksxh:
            if hasattr(self.jksxh, 'to_alipay_dict'):
                params['jksxh'] = self.jksxh.to_alipay_dict()
            else:
                params['jksxh'] = self.jksxh
        if self.mortgage_no:
            if hasattr(self.mortgage_no, 'to_alipay_dict'):
                params['mortgage_no'] = self.mortgage_no.to_alipay_dict()
            else:
                params['mortgage_no'] = self.mortgage_no
        if self.out_mortgage_no:
            if hasattr(self.out_mortgage_no, 'to_alipay_dict'):
                params['out_mortgage_no'] = self.out_mortgage_no.to_alipay_dict()
            else:
                params['out_mortgage_no'] = self.out_mortgage_no
        if self.pre_mortgage_info:
            if hasattr(self.pre_mortgage_info, 'to_alipay_dict'):
                params['pre_mortgage_info'] = self.pre_mortgage_info.to_alipay_dict()
            else:
                params['pre_mortgage_info'] = self.pre_mortgage_info
        if self.proxy_invalid_file_list:
            if isinstance(self.proxy_invalid_file_list, list):
                for i in range(0, len(self.proxy_invalid_file_list)):
                    element = self.proxy_invalid_file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.proxy_invalid_file_list[i] = element.to_alipay_dict()
            if hasattr(self.proxy_invalid_file_list, 'to_alipay_dict'):
                params['proxy_invalid_file_list'] = self.proxy_invalid_file_list.to_alipay_dict()
            else:
                params['proxy_invalid_file_list'] = self.proxy_invalid_file_list
        if self.receiver_info:
            if hasattr(self.receiver_info, 'to_alipay_dict'):
                params['receiver_info'] = self.receiver_info.to_alipay_dict()
            else:
                params['receiver_info'] = self.receiver_info
        if self.refuse_msg:
            if hasattr(self.refuse_msg, 'to_alipay_dict'):
                params['refuse_msg'] = self.refuse_msg.to_alipay_dict()
            else:
                params['refuse_msg'] = self.refuse_msg
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.supple_agreement_list:
            if isinstance(self.supple_agreement_list, list):
                for i in range(0, len(self.supple_agreement_list)):
                    element = self.supple_agreement_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.supple_agreement_list[i] = element.to_alipay_dict()
            if hasattr(self.supple_agreement_list, 'to_alipay_dict'):
                params['supple_agreement_list'] = self.supple_agreement_list.to_alipay_dict()
            else:
                params['supple_agreement_list'] = self.supple_agreement_list
        if self.supple_file_list:
            if isinstance(self.supple_file_list, list):
                for i in range(0, len(self.supple_file_list)):
                    element = self.supple_file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.supple_file_list[i] = element.to_alipay_dict()
            if hasattr(self.supple_file_list, 'to_alipay_dict'):
                params['supple_file_list'] = self.supple_file_list.to_alipay_dict()
            else:
                params['supple_file_list'] = self.supple_file_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistCarfinMortgageapplystatusNotifyModel()
        if 'jksxh' in d:
            o.jksxh = d['jksxh']
        if 'mortgage_no' in d:
            o.mortgage_no = d['mortgage_no']
        if 'out_mortgage_no' in d:
            o.out_mortgage_no = d['out_mortgage_no']
        if 'pre_mortgage_info' in d:
            o.pre_mortgage_info = d['pre_mortgage_info']
        if 'proxy_invalid_file_list' in d:
            o.proxy_invalid_file_list = d['proxy_invalid_file_list']
        if 'receiver_info' in d:
            o.receiver_info = d['receiver_info']
        if 'refuse_msg' in d:
            o.refuse_msg = d['refuse_msg']
        if 'status' in d:
            o.status = d['status']
        if 'supple_agreement_list' in d:
            o.supple_agreement_list = d['supple_agreement_list']
        if 'supple_file_list' in d:
            o.supple_file_list = d['supple_file_list']
        return o


