#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardRechargeDetail import CardRechargeDetail


class AlipayInsSceneFlowcardRechargeNotifyModel(object):

    def __init__(self):
        self._biz_no = None
        self._iccid = None
        self._recharge_detail = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def iccid(self):
        return self._iccid

    @iccid.setter
    def iccid(self, value):
        self._iccid = value
    @property
    def recharge_detail(self):
        return self._recharge_detail

    @recharge_detail.setter
    def recharge_detail(self, value):
        if isinstance(value, CardRechargeDetail):
            self._recharge_detail = value
        else:
            self._recharge_detail = CardRechargeDetail.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.iccid:
            if hasattr(self.iccid, 'to_alipay_dict'):
                params['iccid'] = self.iccid.to_alipay_dict()
            else:
                params['iccid'] = self.iccid
        if self.recharge_detail:
            if hasattr(self.recharge_detail, 'to_alipay_dict'):
                params['recharge_detail'] = self.recharge_detail.to_alipay_dict()
            else:
                params['recharge_detail'] = self.recharge_detail
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneFlowcardRechargeNotifyModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'iccid' in d:
            o.iccid = d['iccid']
        if 'recharge_detail' in d:
            o.recharge_detail = d['recharge_detail']
        return o


