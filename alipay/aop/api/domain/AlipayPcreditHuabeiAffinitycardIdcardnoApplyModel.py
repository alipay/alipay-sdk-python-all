#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiAffinitycardIdcardnoApplyModel(object):

    def __init__(self):
        self._biz_scene = None
        self._id_card_no = None
        self._merchant_partner_id = None
        self._mobile = None
        self._out_biz_no = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def id_card_no(self):
        return self._id_card_no

    @id_card_no.setter
    def id_card_no(self, value):
        self._id_card_no = value
    @property
    def merchant_partner_id(self):
        return self._merchant_partner_id

    @merchant_partner_id.setter
    def merchant_partner_id(self, value):
        self._merchant_partner_id = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.id_card_no:
            if hasattr(self.id_card_no, 'to_alipay_dict'):
                params['id_card_no'] = self.id_card_no.to_alipay_dict()
            else:
                params['id_card_no'] = self.id_card_no
        if self.merchant_partner_id:
            if hasattr(self.merchant_partner_id, 'to_alipay_dict'):
                params['merchant_partner_id'] = self.merchant_partner_id.to_alipay_dict()
            else:
                params['merchant_partner_id'] = self.merchant_partner_id
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
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
        o = AlipayPcreditHuabeiAffinitycardIdcardnoApplyModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'id_card_no' in d:
            o.id_card_no = d['id_card_no']
        if 'merchant_partner_id' in d:
            o.merchant_partner_id = d['merchant_partner_id']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


