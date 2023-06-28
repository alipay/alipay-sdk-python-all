#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneCommonGroupendorseSubmitModel(object):

    def __init__(self):
        self._endorse_fee = None
        self._out_biz_no = None
        self._partner_org_id = None
        self._scene_code = None
        self._sub_order_count = None
        self._summary_endorse_order_no = None
        self._summary_premium = None

    @property
    def endorse_fee(self):
        return self._endorse_fee

    @endorse_fee.setter
    def endorse_fee(self, value):
        self._endorse_fee = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def sub_order_count(self):
        return self._sub_order_count

    @sub_order_count.setter
    def sub_order_count(self, value):
        self._sub_order_count = value
    @property
    def summary_endorse_order_no(self):
        return self._summary_endorse_order_no

    @summary_endorse_order_no.setter
    def summary_endorse_order_no(self, value):
        self._summary_endorse_order_no = value
    @property
    def summary_premium(self):
        return self._summary_premium

    @summary_premium.setter
    def summary_premium(self, value):
        self._summary_premium = value


    def to_alipay_dict(self):
        params = dict()
        if self.endorse_fee:
            if hasattr(self.endorse_fee, 'to_alipay_dict'):
                params['endorse_fee'] = self.endorse_fee.to_alipay_dict()
            else:
                params['endorse_fee'] = self.endorse_fee
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.sub_order_count:
            if hasattr(self.sub_order_count, 'to_alipay_dict'):
                params['sub_order_count'] = self.sub_order_count.to_alipay_dict()
            else:
                params['sub_order_count'] = self.sub_order_count
        if self.summary_endorse_order_no:
            if hasattr(self.summary_endorse_order_no, 'to_alipay_dict'):
                params['summary_endorse_order_no'] = self.summary_endorse_order_no.to_alipay_dict()
            else:
                params['summary_endorse_order_no'] = self.summary_endorse_order_no
        if self.summary_premium:
            if hasattr(self.summary_premium, 'to_alipay_dict'):
                params['summary_premium'] = self.summary_premium.to_alipay_dict()
            else:
                params['summary_premium'] = self.summary_premium
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneCommonGroupendorseSubmitModel()
        if 'endorse_fee' in d:
            o.endorse_fee = d['endorse_fee']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'sub_order_count' in d:
            o.sub_order_count = d['sub_order_count']
        if 'summary_endorse_order_no' in d:
            o.summary_endorse_order_no = d['summary_endorse_order_no']
        if 'summary_premium' in d:
            o.summary_premium = d['summary_premium']
        return o


