#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PointCard import PointCard
from alipay.aop.api.domain.SendRule import SendRule
from alipay.aop.api.domain.Voucher import Voucher


class PromoTool(object):

    def __init__(self):
        self._point_card = None
        self._send_rule = None
        self._status = None
        self._voucher = None
        self._voucher_no = None

    @property
    def point_card(self):
        return self._point_card

    @point_card.setter
    def point_card(self, value):
        if isinstance(value, PointCard):
            self._point_card = value
        else:
            self._point_card = PointCard.from_alipay_dict(value)
    @property
    def send_rule(self):
        return self._send_rule

    @send_rule.setter
    def send_rule(self, value):
        if isinstance(value, SendRule):
            self._send_rule = value
        else:
            self._send_rule = SendRule.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def voucher(self):
        return self._voucher

    @voucher.setter
    def voucher(self, value):
        if isinstance(value, Voucher):
            self._voucher = value
        else:
            self._voucher = Voucher.from_alipay_dict(value)
    @property
    def voucher_no(self):
        return self._voucher_no

    @voucher_no.setter
    def voucher_no(self, value):
        self._voucher_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.point_card:
            if hasattr(self.point_card, 'to_alipay_dict'):
                params['point_card'] = self.point_card.to_alipay_dict()
            else:
                params['point_card'] = self.point_card
        if self.send_rule:
            if hasattr(self.send_rule, 'to_alipay_dict'):
                params['send_rule'] = self.send_rule.to_alipay_dict()
            else:
                params['send_rule'] = self.send_rule
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.voucher:
            if hasattr(self.voucher, 'to_alipay_dict'):
                params['voucher'] = self.voucher.to_alipay_dict()
            else:
                params['voucher'] = self.voucher
        if self.voucher_no:
            if hasattr(self.voucher_no, 'to_alipay_dict'):
                params['voucher_no'] = self.voucher_no.to_alipay_dict()
            else:
                params['voucher_no'] = self.voucher_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoTool()
        if 'point_card' in d:
            o.point_card = d['point_card']
        if 'send_rule' in d:
            o.send_rule = d['send_rule']
        if 'status' in d:
            o.status = d['status']
        if 'voucher' in d:
            o.voucher = d['voucher']
        if 'voucher_no' in d:
            o.voucher_no = d['voucher_no']
        return o


