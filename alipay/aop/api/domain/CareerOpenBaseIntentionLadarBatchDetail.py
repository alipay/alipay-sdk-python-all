#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CareerOpenBaseIntentionLadarBatchDetail(object):

    def __init__(self):
        self._encrypted_id_card = None
        self._encrypted_mobile = None
        self._idfa = None
        self._imei = None
        self._oaid = None
        self._out_biz_no = None

    @property
    def encrypted_id_card(self):
        return self._encrypted_id_card

    @encrypted_id_card.setter
    def encrypted_id_card(self, value):
        self._encrypted_id_card = value
    @property
    def encrypted_mobile(self):
        return self._encrypted_mobile

    @encrypted_mobile.setter
    def encrypted_mobile(self, value):
        self._encrypted_mobile = value
    @property
    def idfa(self):
        return self._idfa

    @idfa.setter
    def idfa(self, value):
        self._idfa = value
    @property
    def imei(self):
        return self._imei

    @imei.setter
    def imei(self, value):
        self._imei = value
    @property
    def oaid(self):
        return self._oaid

    @oaid.setter
    def oaid(self, value):
        self._oaid = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.encrypted_id_card:
            if hasattr(self.encrypted_id_card, 'to_alipay_dict'):
                params['encrypted_id_card'] = self.encrypted_id_card.to_alipay_dict()
            else:
                params['encrypted_id_card'] = self.encrypted_id_card
        if self.encrypted_mobile:
            if hasattr(self.encrypted_mobile, 'to_alipay_dict'):
                params['encrypted_mobile'] = self.encrypted_mobile.to_alipay_dict()
            else:
                params['encrypted_mobile'] = self.encrypted_mobile
        if self.idfa:
            if hasattr(self.idfa, 'to_alipay_dict'):
                params['idfa'] = self.idfa.to_alipay_dict()
            else:
                params['idfa'] = self.idfa
        if self.imei:
            if hasattr(self.imei, 'to_alipay_dict'):
                params['imei'] = self.imei.to_alipay_dict()
            else:
                params['imei'] = self.imei
        if self.oaid:
            if hasattr(self.oaid, 'to_alipay_dict'):
                params['oaid'] = self.oaid.to_alipay_dict()
            else:
                params['oaid'] = self.oaid
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CareerOpenBaseIntentionLadarBatchDetail()
        if 'encrypted_id_card' in d:
            o.encrypted_id_card = d['encrypted_id_card']
        if 'encrypted_mobile' in d:
            o.encrypted_mobile = d['encrypted_mobile']
        if 'idfa' in d:
            o.idfa = d['idfa']
        if 'imei' in d:
            o.imei = d['imei']
        if 'oaid' in d:
            o.oaid = d['oaid']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


