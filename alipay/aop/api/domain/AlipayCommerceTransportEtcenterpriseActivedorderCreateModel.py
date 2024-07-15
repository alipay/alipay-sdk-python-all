#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcenterpriseActivedorderCreateModel(object):

    def __init__(self):
        self._agent_cert_no = None
        self._agent_cert_type = None
        self._agent_name = None
        self._biz_time = None
        self._card_no = None
        self._city_code = None
        self._corp_id = None
        self._device_no = None
        self._engine_no = None
        self._mobile_no = None
        self._order_status = None
        self._out_biz_no = None
        self._plate_color = None
        self._plate_no = None
        self._seller_id = None
        self._vi_ac = None
        self._vi_grant_date = None
        self._vi_gross_mass = None
        self._vi_height = None
        self._vi_length = None
        self._vi_model_name = None
        self._vi_owner_name = None
        self._vi_register_date = None
        self._vi_vin = None
        self._vi_width = None

    @property
    def agent_cert_no(self):
        return self._agent_cert_no

    @agent_cert_no.setter
    def agent_cert_no(self, value):
        self._agent_cert_no = value
    @property
    def agent_cert_type(self):
        return self._agent_cert_type

    @agent_cert_type.setter
    def agent_cert_type(self, value):
        self._agent_cert_type = value
    @property
    def agent_name(self):
        return self._agent_name

    @agent_name.setter
    def agent_name(self, value):
        self._agent_name = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def corp_id(self):
        return self._corp_id

    @corp_id.setter
    def corp_id(self, value):
        self._corp_id = value
    @property
    def device_no(self):
        return self._device_no

    @device_no.setter
    def device_no(self, value):
        self._device_no = value
    @property
    def engine_no(self):
        return self._engine_no

    @engine_no.setter
    def engine_no(self, value):
        self._engine_no = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
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
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def vi_ac(self):
        return self._vi_ac

    @vi_ac.setter
    def vi_ac(self, value):
        self._vi_ac = value
    @property
    def vi_grant_date(self):
        return self._vi_grant_date

    @vi_grant_date.setter
    def vi_grant_date(self, value):
        self._vi_grant_date = value
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
    def vi_model_name(self):
        return self._vi_model_name

    @vi_model_name.setter
    def vi_model_name(self, value):
        self._vi_model_name = value
    @property
    def vi_owner_name(self):
        return self._vi_owner_name

    @vi_owner_name.setter
    def vi_owner_name(self, value):
        self._vi_owner_name = value
    @property
    def vi_register_date(self):
        return self._vi_register_date

    @vi_register_date.setter
    def vi_register_date(self, value):
        self._vi_register_date = value
    @property
    def vi_vin(self):
        return self._vi_vin

    @vi_vin.setter
    def vi_vin(self, value):
        self._vi_vin = value
    @property
    def vi_width(self):
        return self._vi_width

    @vi_width.setter
    def vi_width(self, value):
        self._vi_width = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_cert_no:
            if hasattr(self.agent_cert_no, 'to_alipay_dict'):
                params['agent_cert_no'] = self.agent_cert_no.to_alipay_dict()
            else:
                params['agent_cert_no'] = self.agent_cert_no
        if self.agent_cert_type:
            if hasattr(self.agent_cert_type, 'to_alipay_dict'):
                params['agent_cert_type'] = self.agent_cert_type.to_alipay_dict()
            else:
                params['agent_cert_type'] = self.agent_cert_type
        if self.agent_name:
            if hasattr(self.agent_name, 'to_alipay_dict'):
                params['agent_name'] = self.agent_name.to_alipay_dict()
            else:
                params['agent_name'] = self.agent_name
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.corp_id:
            if hasattr(self.corp_id, 'to_alipay_dict'):
                params['corp_id'] = self.corp_id.to_alipay_dict()
            else:
                params['corp_id'] = self.corp_id
        if self.device_no:
            if hasattr(self.device_no, 'to_alipay_dict'):
                params['device_no'] = self.device_no.to_alipay_dict()
            else:
                params['device_no'] = self.device_no
        if self.engine_no:
            if hasattr(self.engine_no, 'to_alipay_dict'):
                params['engine_no'] = self.engine_no.to_alipay_dict()
            else:
                params['engine_no'] = self.engine_no
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
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
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.vi_ac:
            if hasattr(self.vi_ac, 'to_alipay_dict'):
                params['vi_ac'] = self.vi_ac.to_alipay_dict()
            else:
                params['vi_ac'] = self.vi_ac
        if self.vi_grant_date:
            if hasattr(self.vi_grant_date, 'to_alipay_dict'):
                params['vi_grant_date'] = self.vi_grant_date.to_alipay_dict()
            else:
                params['vi_grant_date'] = self.vi_grant_date
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
        if self.vi_model_name:
            if hasattr(self.vi_model_name, 'to_alipay_dict'):
                params['vi_model_name'] = self.vi_model_name.to_alipay_dict()
            else:
                params['vi_model_name'] = self.vi_model_name
        if self.vi_owner_name:
            if hasattr(self.vi_owner_name, 'to_alipay_dict'):
                params['vi_owner_name'] = self.vi_owner_name.to_alipay_dict()
            else:
                params['vi_owner_name'] = self.vi_owner_name
        if self.vi_register_date:
            if hasattr(self.vi_register_date, 'to_alipay_dict'):
                params['vi_register_date'] = self.vi_register_date.to_alipay_dict()
            else:
                params['vi_register_date'] = self.vi_register_date
        if self.vi_vin:
            if hasattr(self.vi_vin, 'to_alipay_dict'):
                params['vi_vin'] = self.vi_vin.to_alipay_dict()
            else:
                params['vi_vin'] = self.vi_vin
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
        o = AlipayCommerceTransportEtcenterpriseActivedorderCreateModel()
        if 'agent_cert_no' in d:
            o.agent_cert_no = d['agent_cert_no']
        if 'agent_cert_type' in d:
            o.agent_cert_type = d['agent_cert_type']
        if 'agent_name' in d:
            o.agent_name = d['agent_name']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'device_no' in d:
            o.device_no = d['device_no']
        if 'engine_no' in d:
            o.engine_no = d['engine_no']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'vi_ac' in d:
            o.vi_ac = d['vi_ac']
        if 'vi_grant_date' in d:
            o.vi_grant_date = d['vi_grant_date']
        if 'vi_gross_mass' in d:
            o.vi_gross_mass = d['vi_gross_mass']
        if 'vi_height' in d:
            o.vi_height = d['vi_height']
        if 'vi_length' in d:
            o.vi_length = d['vi_length']
        if 'vi_model_name' in d:
            o.vi_model_name = d['vi_model_name']
        if 'vi_owner_name' in d:
            o.vi_owner_name = d['vi_owner_name']
        if 'vi_register_date' in d:
            o.vi_register_date = d['vi_register_date']
        if 'vi_vin' in d:
            o.vi_vin = d['vi_vin']
        if 'vi_width' in d:
            o.vi_width = d['vi_width']
        return o


