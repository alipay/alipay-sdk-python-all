#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CommercializationCertificateInfo import CommercializationCertificateInfo


class AlipayEcoMycarCommercializationCertificateFreezeModel(object):

    def __init__(self):
        self._ant_store_id = None
        self._certificate_use_info_list = None
        self._open_id = None
        self._operate_serial_number = None
        self._operate_time = None
        self._out_biz_order_id = None
        self._user_id = None

    @property
    def ant_store_id(self):
        return self._ant_store_id

    @ant_store_id.setter
    def ant_store_id(self, value):
        self._ant_store_id = value
    @property
    def certificate_use_info_list(self):
        return self._certificate_use_info_list

    @certificate_use_info_list.setter
    def certificate_use_info_list(self, value):
        if isinstance(value, list):
            self._certificate_use_info_list = list()
            for i in value:
                if isinstance(i, CommercializationCertificateInfo):
                    self._certificate_use_info_list.append(i)
                else:
                    self._certificate_use_info_list.append(CommercializationCertificateInfo.from_alipay_dict(i))
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def operate_serial_number(self):
        return self._operate_serial_number

    @operate_serial_number.setter
    def operate_serial_number(self, value):
        self._operate_serial_number = value
    @property
    def operate_time(self):
        return self._operate_time

    @operate_time.setter
    def operate_time(self, value):
        self._operate_time = value
    @property
    def out_biz_order_id(self):
        return self._out_biz_order_id

    @out_biz_order_id.setter
    def out_biz_order_id(self, value):
        self._out_biz_order_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_store_id:
            if hasattr(self.ant_store_id, 'to_alipay_dict'):
                params['ant_store_id'] = self.ant_store_id.to_alipay_dict()
            else:
                params['ant_store_id'] = self.ant_store_id
        if self.certificate_use_info_list:
            if isinstance(self.certificate_use_info_list, list):
                for i in range(0, len(self.certificate_use_info_list)):
                    element = self.certificate_use_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.certificate_use_info_list[i] = element.to_alipay_dict()
            if hasattr(self.certificate_use_info_list, 'to_alipay_dict'):
                params['certificate_use_info_list'] = self.certificate_use_info_list.to_alipay_dict()
            else:
                params['certificate_use_info_list'] = self.certificate_use_info_list
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.operate_serial_number:
            if hasattr(self.operate_serial_number, 'to_alipay_dict'):
                params['operate_serial_number'] = self.operate_serial_number.to_alipay_dict()
            else:
                params['operate_serial_number'] = self.operate_serial_number
        if self.operate_time:
            if hasattr(self.operate_time, 'to_alipay_dict'):
                params['operate_time'] = self.operate_time.to_alipay_dict()
            else:
                params['operate_time'] = self.operate_time
        if self.out_biz_order_id:
            if hasattr(self.out_biz_order_id, 'to_alipay_dict'):
                params['out_biz_order_id'] = self.out_biz_order_id.to_alipay_dict()
            else:
                params['out_biz_order_id'] = self.out_biz_order_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarCommercializationCertificateFreezeModel()
        if 'ant_store_id' in d:
            o.ant_store_id = d['ant_store_id']
        if 'certificate_use_info_list' in d:
            o.certificate_use_info_list = d['certificate_use_info_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'operate_serial_number' in d:
            o.operate_serial_number = d['operate_serial_number']
        if 'operate_time' in d:
            o.operate_time = d['operate_time']
        if 'out_biz_order_id' in d:
            o.out_biz_order_id = d['out_biz_order_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


