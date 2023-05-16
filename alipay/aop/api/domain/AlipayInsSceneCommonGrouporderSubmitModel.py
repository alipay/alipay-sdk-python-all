#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneCommonGrouporderSubmitModel(object):

    def __init__(self):
        self._out_biz_no = None
        self._partner_org_id = None
        self._scene_code = None
        self._sub_order_count = None
        self._summary_order_no = None
        self._summary_order_premium = None

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
    def summary_order_no(self):
        return self._summary_order_no

    @summary_order_no.setter
    def summary_order_no(self, value):
        self._summary_order_no = value
    @property
    def summary_order_premium(self):
        return self._summary_order_premium

    @summary_order_premium.setter
    def summary_order_premium(self, value):
        self._summary_order_premium = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.summary_order_no:
            if hasattr(self.summary_order_no, 'to_alipay_dict'):
                params['summary_order_no'] = self.summary_order_no.to_alipay_dict()
            else:
                params['summary_order_no'] = self.summary_order_no
        if self.summary_order_premium:
            if hasattr(self.summary_order_premium, 'to_alipay_dict'):
                params['summary_order_premium'] = self.summary_order_premium.to_alipay_dict()
            else:
                params['summary_order_premium'] = self.summary_order_premium
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneCommonGrouporderSubmitModel()
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'sub_order_count' in d:
            o.sub_order_count = d['sub_order_count']
        if 'summary_order_no' in d:
            o.summary_order_no = d['summary_order_no']
        if 'summary_order_premium' in d:
            o.summary_order_premium = d['summary_order_premium']
        return o


