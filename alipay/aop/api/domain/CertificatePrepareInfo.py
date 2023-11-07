#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CertificateInstanceAmountInfo import CertificateInstanceAmountInfo
from alipay.aop.api.domain.CertificateSkuInfo import CertificateSkuInfo
from alipay.aop.api.domain.CertificateTimesCardInfo import CertificateTimesCardInfo


class CertificatePrepareInfo(object):

    def __init__(self):
        self._amount_info = None
        self._certificate_id = None
        self._encrypted_code = None
        self._order_id = None
        self._sku_info = None
        self._times_card_info = None
        self._valid_begin_time = None
        self._valid_end_time = None

    @property
    def amount_info(self):
        return self._amount_info

    @amount_info.setter
    def amount_info(self, value):
        if isinstance(value, CertificateInstanceAmountInfo):
            self._amount_info = value
        else:
            self._amount_info = CertificateInstanceAmountInfo.from_alipay_dict(value)
    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def encrypted_code(self):
        return self._encrypted_code

    @encrypted_code.setter
    def encrypted_code(self, value):
        self._encrypted_code = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def sku_info(self):
        return self._sku_info

    @sku_info.setter
    def sku_info(self, value):
        if isinstance(value, CertificateSkuInfo):
            self._sku_info = value
        else:
            self._sku_info = CertificateSkuInfo.from_alipay_dict(value)
    @property
    def times_card_info(self):
        return self._times_card_info

    @times_card_info.setter
    def times_card_info(self, value):
        if isinstance(value, CertificateTimesCardInfo):
            self._times_card_info = value
        else:
            self._times_card_info = CertificateTimesCardInfo.from_alipay_dict(value)
    @property
    def valid_begin_time(self):
        return self._valid_begin_time

    @valid_begin_time.setter
    def valid_begin_time(self, value):
        self._valid_begin_time = value
    @property
    def valid_end_time(self):
        return self._valid_end_time

    @valid_end_time.setter
    def valid_end_time(self, value):
        self._valid_end_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_info:
            if hasattr(self.amount_info, 'to_alipay_dict'):
                params['amount_info'] = self.amount_info.to_alipay_dict()
            else:
                params['amount_info'] = self.amount_info
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.encrypted_code:
            if hasattr(self.encrypted_code, 'to_alipay_dict'):
                params['encrypted_code'] = self.encrypted_code.to_alipay_dict()
            else:
                params['encrypted_code'] = self.encrypted_code
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.sku_info:
            if hasattr(self.sku_info, 'to_alipay_dict'):
                params['sku_info'] = self.sku_info.to_alipay_dict()
            else:
                params['sku_info'] = self.sku_info
        if self.times_card_info:
            if hasattr(self.times_card_info, 'to_alipay_dict'):
                params['times_card_info'] = self.times_card_info.to_alipay_dict()
            else:
                params['times_card_info'] = self.times_card_info
        if self.valid_begin_time:
            if hasattr(self.valid_begin_time, 'to_alipay_dict'):
                params['valid_begin_time'] = self.valid_begin_time.to_alipay_dict()
            else:
                params['valid_begin_time'] = self.valid_begin_time
        if self.valid_end_time:
            if hasattr(self.valid_end_time, 'to_alipay_dict'):
                params['valid_end_time'] = self.valid_end_time.to_alipay_dict()
            else:
                params['valid_end_time'] = self.valid_end_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertificatePrepareInfo()
        if 'amount_info' in d:
            o.amount_info = d['amount_info']
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'encrypted_code' in d:
            o.encrypted_code = d['encrypted_code']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'sku_info' in d:
            o.sku_info = d['sku_info']
        if 'times_card_info' in d:
            o.times_card_info = d['times_card_info']
        if 'valid_begin_time' in d:
            o.valid_begin_time = d['valid_begin_time']
        if 'valid_end_time' in d:
            o.valid_end_time = d['valid_end_time']
        return o


