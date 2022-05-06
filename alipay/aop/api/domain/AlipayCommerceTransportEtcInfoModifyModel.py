#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcInfoModifyModel(object):

    def __init__(self):
        self._biz_agreement_no = None
        self._card_no = None
        self._device_no = None
        self._order_id = None
        self._out_biz_no = None
        self._plate_color = None
        self._plate_no = None
        self._user_id = None
        self._vi_ac = None
        self._vi_gross_mass = None
        self._vi_height = None
        self._vi_length = None
        self._vi_owner_name = None
        self._vi_width = None

    @property
    def biz_agreement_no(self):
        return self._biz_agreement_no

    @biz_agreement_no.setter
    def biz_agreement_no(self, value):
        self._biz_agreement_no = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def device_no(self):
        return self._device_no

    @device_no.setter
    def device_no(self, value):
        self._device_no = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def plate_color(self):
        return self._plate_color

    @plate_color.setter
    def plate_color(self, value):
        self._plate_color = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def vi_ac(self):
        return self._vi_ac

    @vi_ac.setter
    def vi_ac(self, value):
        self._vi_ac = value
    @property
    def vi_gross_mass(self):
        return self._vi_gross_mass

    @vi_gross_mass.setter
    def vi_gross_mass(self, value):
        self._vi_gross_mass = value
    @property
    def vi_height(self):
        return self._vi_height

    @vi_height.setter
    def vi_height(self, value):
        self._vi_height = value
    @property
    def vi_length(self):
        return self._vi_length

    @vi_length.setter
    def vi_length(self, value):
        self._vi_length = value
    @property
    def vi_owner_name(self):
        return self._vi_owner_name

    @vi_owner_name.setter
    def vi_owner_name(self, value):
        self._vi_owner_name = value
    @property
    def vi_width(self):
        return self._vi_width

    @vi_width.setter
    def vi_width(self, value):
        self._vi_width = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_agreement_no:
            if hasattr(self.biz_agreement_no, 'to_alipay_dict'):
                params['biz_agreement_no'] = self.biz_agreement_no.to_alipay_dict()
            else:
                params['biz_agreement_no'] = self.biz_agreement_no
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.device_no:
            if hasattr(self.device_no, 'to_alipay_dict'):
                params['device_no'] = self.device_no.to_alipay_dict()
            else:
                params['device_no'] = self.device_no
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.plate_color:
            if hasattr(self.plate_color, 'to_alipay_dict'):
                params['plate_color'] = self.plate_color.to_alipay_dict()
            else:
                params['plate_color'] = self.plate_color
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.vi_ac:
            if hasattr(self.vi_ac, 'to_alipay_dict'):
                params['vi_ac'] = self.vi_ac.to_alipay_dict()
            else:
                params['vi_ac'] = self.vi_ac
        if self.vi_gross_mass:
            if hasattr(self.vi_gross_mass, 'to_alipay_dict'):
                params['vi_gross_mass'] = self.vi_gross_mass.to_alipay_dict()
            else:
                params['vi_gross_mass'] = self.vi_gross_mass
        if self.vi_height:
            if hasattr(self.vi_height, 'to_alipay_dict'):
                params['vi_height'] = self.vi_height.to_alipay_dict()
            else:
                params['vi_height'] = self.vi_height
        if self.vi_length:
            if hasattr(self.vi_length, 'to_alipay_dict'):
                params['vi_length'] = self.vi_length.to_alipay_dict()
            else:
                params['vi_length'] = self.vi_length
        if self.vi_owner_name:
            if hasattr(self.vi_owner_name, 'to_alipay_dict'):
                params['vi_owner_name'] = self.vi_owner_name.to_alipay_dict()
            else:
                params['vi_owner_name'] = self.vi_owner_name
        if self.vi_width:
            if hasattr(self.vi_width, 'to_alipay_dict'):
                params['vi_width'] = self.vi_width.to_alipay_dict()
            else:
                params['vi_width'] = self.vi_width
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcInfoModifyModel()
        if 'biz_agreement_no' in d:
            o.biz_agreement_no = d['biz_agreement_no']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'device_no' in d:
            o.device_no = d['device_no']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'vi_ac' in d:
            o.vi_ac = d['vi_ac']
        if 'vi_gross_mass' in d:
            o.vi_gross_mass = d['vi_gross_mass']
        if 'vi_height' in d:
            o.vi_height = d['vi_height']
        if 'vi_length' in d:
            o.vi_length = d['vi_length']
        if 'vi_owner_name' in d:
            o.vi_owner_name = d['vi_owner_name']
        if 'vi_width' in d:
            o.vi_width = d['vi_width']
        return o


