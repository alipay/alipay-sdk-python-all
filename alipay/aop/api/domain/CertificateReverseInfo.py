#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertificateReverseInfo(object):

    def __init__(self):
        self._certificate_id = None
        self._serial_no_list = None
        self._times_card_cancel_count = None
        self._use_order_no = None

    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def serial_no_list(self):
        return self._serial_no_list

    @serial_no_list.setter
    def serial_no_list(self, value):
        if isinstance(value, list):
            self._serial_no_list = list()
            for i in value:
                self._serial_no_list.append(i)
    @property
    def times_card_cancel_count(self):
        return self._times_card_cancel_count

    @times_card_cancel_count.setter
    def times_card_cancel_count(self, value):
        self._times_card_cancel_count = value
    @property
    def use_order_no(self):
        return self._use_order_no

    @use_order_no.setter
    def use_order_no(self, value):
        self._use_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.serial_no_list:
            if isinstance(self.serial_no_list, list):
                for i in range(0, len(self.serial_no_list)):
                    element = self.serial_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.serial_no_list[i] = element.to_alipay_dict()
            if hasattr(self.serial_no_list, 'to_alipay_dict'):
                params['serial_no_list'] = self.serial_no_list.to_alipay_dict()
            else:
                params['serial_no_list'] = self.serial_no_list
        if self.times_card_cancel_count:
            if hasattr(self.times_card_cancel_count, 'to_alipay_dict'):
                params['times_card_cancel_count'] = self.times_card_cancel_count.to_alipay_dict()
            else:
                params['times_card_cancel_count'] = self.times_card_cancel_count
        if self.use_order_no:
            if hasattr(self.use_order_no, 'to_alipay_dict'):
                params['use_order_no'] = self.use_order_no.to_alipay_dict()
            else:
                params['use_order_no'] = self.use_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertificateReverseInfo()
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'serial_no_list' in d:
            o.serial_no_list = d['serial_no_list']
        if 'times_card_cancel_count' in d:
            o.times_card_cancel_count = d['times_card_cancel_count']
        if 'use_order_no' in d:
            o.use_order_no = d['use_order_no']
        return o


