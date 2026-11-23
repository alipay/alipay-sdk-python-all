#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CertificateGoodsInfo import CertificateGoodsInfo


class CertificateSimpleInfo(object):

    def __init__(self):
        self._certificate_id = None
        self._encrypted_data = None
        self._goods = None
        self._open_id = None
        self._user_id = None

    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def encrypted_data(self):
        return self._encrypted_data

    @encrypted_data.setter
    def encrypted_data(self, value):
        self._encrypted_data = value
    @property
    def goods(self):
        return self._goods

    @goods.setter
    def goods(self, value):
        if isinstance(value, list):
            self._goods = list()
            for i in value:
                if isinstance(i, CertificateGoodsInfo):
                    self._goods.append(i)
                else:
                    self._goods.append(CertificateGoodsInfo.from_alipay_dict(i))
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.encrypted_data:
            if hasattr(self.encrypted_data, 'to_alipay_dict'):
                params['encrypted_data'] = self.encrypted_data.to_alipay_dict()
            else:
                params['encrypted_data'] = self.encrypted_data
        if self.goods:
            if isinstance(self.goods, list):
                for i in range(0, len(self.goods)):
                    element = self.goods[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods[i] = element.to_alipay_dict()
            if hasattr(self.goods, 'to_alipay_dict'):
                params['goods'] = self.goods.to_alipay_dict()
            else:
                params['goods'] = self.goods
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = CertificateSimpleInfo()
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'encrypted_data' in d:
            o.encrypted_data = d['encrypted_data']
        if 'goods' in d:
            o.goods = d['goods']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


