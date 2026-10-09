#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CareerOpenBaseIntentionLadarDetailResult(object):

    def __init__(self):
        self._desc_msg = None
        self._detail_status = None
        self._encrypted_id_card = None
        self._encrypted_mobile = None
        self._idfa = None
        self._imei = None
        self._oaid = None
        self._out_biz_no = None
        self._score = None

    @property
    def desc_msg(self):
        return self._desc_msg

    @desc_msg.setter
    def desc_msg(self, value):
        self._desc_msg = value
    @property
    def detail_status(self):
        return self._detail_status

    @detail_status.setter
    def detail_status(self, value):
        self._detail_status = value
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
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc_msg:
            if hasattr(self.desc_msg, 'to_alipay_dict'):
                params['desc_msg'] = self.desc_msg.to_alipay_dict()
            else:
                params['desc_msg'] = self.desc_msg
        if self.detail_status:
            if hasattr(self.detail_status, 'to_alipay_dict'):
                params['detail_status'] = self.detail_status.to_alipay_dict()
            else:
                params['detail_status'] = self.detail_status
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
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CareerOpenBaseIntentionLadarDetailResult()
        if 'desc_msg' in d:
            o.desc_msg = d['desc_msg']
        if 'detail_status' in d:
            o.detail_status = d['detail_status']
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
        if 'score' in d:
            o.score = d['score']
        return o


