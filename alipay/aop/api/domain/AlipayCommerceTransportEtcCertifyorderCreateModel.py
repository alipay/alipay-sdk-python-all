#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcCertifyorderCreateModel(object):

    def __init__(self):
        self._car_type = None
        self._city_code = None
        self._license_img_required_flag = None
        self._mobile_no = None
        self._open_id = None
        self._out_biz_no = None
        self._plate_color = None
        self._plate_no = None
        self._product_id = None
        self._seller_id = None
        self._user_id = None
        self._veh_biz_scene = None
        self._vi_license_engine = None
        self._vi_license_vin = None

    @property
    def car_type(self):
        return self._car_type

    @car_type.setter
    def car_type(self, value):
        self._car_type = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def license_img_required_flag(self):
        return self._license_img_required_flag

    @license_img_required_flag.setter
    def license_img_required_flag(self, value):
        self._license_img_required_flag = value
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
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
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
    def veh_biz_scene(self):
        return self._veh_biz_scene

    @veh_biz_scene.setter
    def veh_biz_scene(self, value):
        self._veh_biz_scene = value
    @property
    def vi_license_engine(self):
        return self._vi_license_engine

    @vi_license_engine.setter
    def vi_license_engine(self, value):
        self._vi_license_engine = value
    @property
    def vi_license_vin(self):
        return self._vi_license_vin

    @vi_license_vin.setter
    def vi_license_vin(self, value):
        self._vi_license_vin = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_type:
            if hasattr(self.car_type, 'to_alipay_dict'):
                params['car_type'] = self.car_type.to_alipay_dict()
            else:
                params['car_type'] = self.car_type
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.license_img_required_flag:
            if hasattr(self.license_img_required_flag, 'to_alipay_dict'):
                params['license_img_required_flag'] = self.license_img_required_flag.to_alipay_dict()
            else:
                params['license_img_required_flag'] = self.license_img_required_flag
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
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
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
        if self.veh_biz_scene:
            if hasattr(self.veh_biz_scene, 'to_alipay_dict'):
                params['veh_biz_scene'] = self.veh_biz_scene.to_alipay_dict()
            else:
                params['veh_biz_scene'] = self.veh_biz_scene
        if self.vi_license_engine:
            if hasattr(self.vi_license_engine, 'to_alipay_dict'):
                params['vi_license_engine'] = self.vi_license_engine.to_alipay_dict()
            else:
                params['vi_license_engine'] = self.vi_license_engine
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
        o = AlipayCommerceTransportEtcCertifyorderCreateModel()
        if 'car_type' in d:
            o.car_type = d['car_type']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'license_img_required_flag' in d:
            o.license_img_required_flag = d['license_img_required_flag']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'veh_biz_scene' in d:
            o.veh_biz_scene = d['veh_biz_scene']
        if 'vi_license_engine' in d:
            o.vi_license_engine = d['vi_license_engine']
        if 'vi_license_vin' in d:
            o.vi_license_vin = d['vi_license_vin']
        return o


