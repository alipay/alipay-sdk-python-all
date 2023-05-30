#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcApplyorderCreateormodifyModel(object):

    def __init__(self):
        self._alipay_order_id = None
        self._apply_scene = None
        self._apply_sub_scene = None
        self._city_code = None
        self._mobile_no = None
        self._open_id = None
        self._order_censor_status = None
        self._order_pay_status = None
        self._out_order_id = None
        self._plate_color = None
        self._plate_no = None
        self._seller_id = None
        self._user_id = None
        self._vi_license_apc = None
        self._vi_license_brand_model = None
        self._vi_license_car_type = None
        self._vi_license_engine = None
        self._vi_license_gross_mass = None
        self._vi_license_issue_date = None
        self._vi_license_overall_dinmension = None
        self._vi_license_owner = None
        self._vi_license_register_date = None
        self._vi_license_unladen_mass = None
        self._vi_license_use_type = None
        self._vi_license_vin = None

    @property
    def alipay_order_id(self):
        return self._alipay_order_id

    @alipay_order_id.setter
    def alipay_order_id(self, value):
        self._alipay_order_id = value
    @property
    def apply_scene(self):
        return self._apply_scene

    @apply_scene.setter
    def apply_scene(self, value):
        self._apply_scene = value
    @property
    def apply_sub_scene(self):
        return self._apply_sub_scene

    @apply_sub_scene.setter
    def apply_sub_scene(self, value):
        self._apply_sub_scene = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_censor_status(self):
        return self._order_censor_status

    @order_censor_status.setter
    def order_censor_status(self, value):
        self._order_censor_status = value
    @property
    def order_pay_status(self):
        return self._order_pay_status

    @order_pay_status.setter
    def order_pay_status(self, value):
        self._order_pay_status = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
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
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def vi_license_apc(self):
        return self._vi_license_apc

    @vi_license_apc.setter
    def vi_license_apc(self, value):
        self._vi_license_apc = value
    @property
    def vi_license_brand_model(self):
        return self._vi_license_brand_model

    @vi_license_brand_model.setter
    def vi_license_brand_model(self, value):
        self._vi_license_brand_model = value
    @property
    def vi_license_car_type(self):
        return self._vi_license_car_type

    @vi_license_car_type.setter
    def vi_license_car_type(self, value):
        self._vi_license_car_type = value
    @property
    def vi_license_engine(self):
        return self._vi_license_engine

    @vi_license_engine.setter
    def vi_license_engine(self, value):
        self._vi_license_engine = value
    @property
    def vi_license_gross_mass(self):
        return self._vi_license_gross_mass

    @vi_license_gross_mass.setter
    def vi_license_gross_mass(self, value):
        self._vi_license_gross_mass = value
    @property
    def vi_license_issue_date(self):
        return self._vi_license_issue_date

    @vi_license_issue_date.setter
    def vi_license_issue_date(self, value):
        self._vi_license_issue_date = value
    @property
    def vi_license_overall_dinmension(self):
        return self._vi_license_overall_dinmension

    @vi_license_overall_dinmension.setter
    def vi_license_overall_dinmension(self, value):
        self._vi_license_overall_dinmension = value
    @property
    def vi_license_owner(self):
        return self._vi_license_owner

    @vi_license_owner.setter
    def vi_license_owner(self, value):
        self._vi_license_owner = value
    @property
    def vi_license_register_date(self):
        return self._vi_license_register_date

    @vi_license_register_date.setter
    def vi_license_register_date(self, value):
        self._vi_license_register_date = value
    @property
    def vi_license_unladen_mass(self):
        return self._vi_license_unladen_mass

    @vi_license_unladen_mass.setter
    def vi_license_unladen_mass(self, value):
        self._vi_license_unladen_mass = value
    @property
    def vi_license_use_type(self):
        return self._vi_license_use_type

    @vi_license_use_type.setter
    def vi_license_use_type(self, value):
        self._vi_license_use_type = value
    @property
    def vi_license_vin(self):
        return self._vi_license_vin

    @vi_license_vin.setter
    def vi_license_vin(self, value):
        self._vi_license_vin = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_order_id:
            if hasattr(self.alipay_order_id, 'to_alipay_dict'):
                params['alipay_order_id'] = self.alipay_order_id.to_alipay_dict()
            else:
                params['alipay_order_id'] = self.alipay_order_id
        if self.apply_scene:
            if hasattr(self.apply_scene, 'to_alipay_dict'):
                params['apply_scene'] = self.apply_scene.to_alipay_dict()
            else:
                params['apply_scene'] = self.apply_scene
        if self.apply_sub_scene:
            if hasattr(self.apply_sub_scene, 'to_alipay_dict'):
                params['apply_sub_scene'] = self.apply_sub_scene.to_alipay_dict()
            else:
                params['apply_sub_scene'] = self.apply_sub_scene
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_censor_status:
            if hasattr(self.order_censor_status, 'to_alipay_dict'):
                params['order_censor_status'] = self.order_censor_status.to_alipay_dict()
            else:
                params['order_censor_status'] = self.order_censor_status
        if self.order_pay_status:
            if hasattr(self.order_pay_status, 'to_alipay_dict'):
                params['order_pay_status'] = self.order_pay_status.to_alipay_dict()
            else:
                params['order_pay_status'] = self.order_pay_status
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
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
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.vi_license_apc:
            if hasattr(self.vi_license_apc, 'to_alipay_dict'):
                params['vi_license_apc'] = self.vi_license_apc.to_alipay_dict()
            else:
                params['vi_license_apc'] = self.vi_license_apc
        if self.vi_license_brand_model:
            if hasattr(self.vi_license_brand_model, 'to_alipay_dict'):
                params['vi_license_brand_model'] = self.vi_license_brand_model.to_alipay_dict()
            else:
                params['vi_license_brand_model'] = self.vi_license_brand_model
        if self.vi_license_car_type:
            if hasattr(self.vi_license_car_type, 'to_alipay_dict'):
                params['vi_license_car_type'] = self.vi_license_car_type.to_alipay_dict()
            else:
                params['vi_license_car_type'] = self.vi_license_car_type
        if self.vi_license_engine:
            if hasattr(self.vi_license_engine, 'to_alipay_dict'):
                params['vi_license_engine'] = self.vi_license_engine.to_alipay_dict()
            else:
                params['vi_license_engine'] = self.vi_license_engine
        if self.vi_license_gross_mass:
            if hasattr(self.vi_license_gross_mass, 'to_alipay_dict'):
                params['vi_license_gross_mass'] = self.vi_license_gross_mass.to_alipay_dict()
            else:
                params['vi_license_gross_mass'] = self.vi_license_gross_mass
        if self.vi_license_issue_date:
            if hasattr(self.vi_license_issue_date, 'to_alipay_dict'):
                params['vi_license_issue_date'] = self.vi_license_issue_date.to_alipay_dict()
            else:
                params['vi_license_issue_date'] = self.vi_license_issue_date
        if self.vi_license_overall_dinmension:
            if hasattr(self.vi_license_overall_dinmension, 'to_alipay_dict'):
                params['vi_license_overall_dinmension'] = self.vi_license_overall_dinmension.to_alipay_dict()
            else:
                params['vi_license_overall_dinmension'] = self.vi_license_overall_dinmension
        if self.vi_license_owner:
            if hasattr(self.vi_license_owner, 'to_alipay_dict'):
                params['vi_license_owner'] = self.vi_license_owner.to_alipay_dict()
            else:
                params['vi_license_owner'] = self.vi_license_owner
        if self.vi_license_register_date:
            if hasattr(self.vi_license_register_date, 'to_alipay_dict'):
                params['vi_license_register_date'] = self.vi_license_register_date.to_alipay_dict()
            else:
                params['vi_license_register_date'] = self.vi_license_register_date
        if self.vi_license_unladen_mass:
            if hasattr(self.vi_license_unladen_mass, 'to_alipay_dict'):
                params['vi_license_unladen_mass'] = self.vi_license_unladen_mass.to_alipay_dict()
            else:
                params['vi_license_unladen_mass'] = self.vi_license_unladen_mass
        if self.vi_license_use_type:
            if hasattr(self.vi_license_use_type, 'to_alipay_dict'):
                params['vi_license_use_type'] = self.vi_license_use_type.to_alipay_dict()
            else:
                params['vi_license_use_type'] = self.vi_license_use_type
        if self.vi_license_vin:
            if hasattr(self.vi_license_vin, 'to_alipay_dict'):
                params['vi_license_vin'] = self.vi_license_vin.to_alipay_dict()
            else:
                params['vi_license_vin'] = self.vi_license_vin
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcApplyorderCreateormodifyModel()
        if 'alipay_order_id' in d:
            o.alipay_order_id = d['alipay_order_id']
        if 'apply_scene' in d:
            o.apply_scene = d['apply_scene']
        if 'apply_sub_scene' in d:
            o.apply_sub_scene = d['apply_sub_scene']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_censor_status' in d:
            o.order_censor_status = d['order_censor_status']
        if 'order_pay_status' in d:
            o.order_pay_status = d['order_pay_status']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'vi_license_apc' in d:
            o.vi_license_apc = d['vi_license_apc']
        if 'vi_license_brand_model' in d:
            o.vi_license_brand_model = d['vi_license_brand_model']
        if 'vi_license_car_type' in d:
            o.vi_license_car_type = d['vi_license_car_type']
        if 'vi_license_engine' in d:
            o.vi_license_engine = d['vi_license_engine']
        if 'vi_license_gross_mass' in d:
            o.vi_license_gross_mass = d['vi_license_gross_mass']
        if 'vi_license_issue_date' in d:
            o.vi_license_issue_date = d['vi_license_issue_date']
        if 'vi_license_overall_dinmension' in d:
            o.vi_license_overall_dinmension = d['vi_license_overall_dinmension']
        if 'vi_license_owner' in d:
            o.vi_license_owner = d['vi_license_owner']
        if 'vi_license_register_date' in d:
            o.vi_license_register_date = d['vi_license_register_date']
        if 'vi_license_unladen_mass' in d:
            o.vi_license_unladen_mass = d['vi_license_unladen_mass']
        if 'vi_license_use_type' in d:
            o.vi_license_use_type = d['vi_license_use_type']
        if 'vi_license_vin' in d:
            o.vi_license_vin = d['vi_license_vin']
        return o


