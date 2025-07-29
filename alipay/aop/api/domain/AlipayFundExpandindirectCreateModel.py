#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SecondaryPartnerInfo import SecondaryPartnerInfo


class AlipayFundExpandindirectCreateModel(object):

    def __init__(self):
        self._biz_scene = None
        self._biz_type = None
        self._original_order_id = None
        self._out_biz_no = None
        self._product_code = None
        self._scene_code = None
        self._scene_directions = None
        self._scene_image = None
        self._scene_qualification_image = None
        self._secondary_partner_info = None
        self._sites = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def original_order_id(self):
        return self._original_order_id

    @original_order_id.setter
    def original_order_id(self, value):
        self._original_order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def scene_directions(self):
        return self._scene_directions

    @scene_directions.setter
    def scene_directions(self, value):
        self._scene_directions = value
    @property
    def scene_image(self):
        return self._scene_image

    @scene_image.setter
    def scene_image(self, value):
        self._scene_image = value
    @property
    def scene_qualification_image(self):
        return self._scene_qualification_image

    @scene_qualification_image.setter
    def scene_qualification_image(self, value):
        self._scene_qualification_image = value
    @property
    def secondary_partner_info(self):
        return self._secondary_partner_info

    @secondary_partner_info.setter
    def secondary_partner_info(self, value):
        if isinstance(value, SecondaryPartnerInfo):
            self._secondary_partner_info = value
        else:
            self._secondary_partner_info = SecondaryPartnerInfo.from_alipay_dict(value)
    @property
    def sites(self):
        return self._sites

    @sites.setter
    def sites(self, value):
        self._sites = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.original_order_id:
            if hasattr(self.original_order_id, 'to_alipay_dict'):
                params['original_order_id'] = self.original_order_id.to_alipay_dict()
            else:
                params['original_order_id'] = self.original_order_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.scene_directions:
            if hasattr(self.scene_directions, 'to_alipay_dict'):
                params['scene_directions'] = self.scene_directions.to_alipay_dict()
            else:
                params['scene_directions'] = self.scene_directions
        if self.scene_image:
            if hasattr(self.scene_image, 'to_alipay_dict'):
                params['scene_image'] = self.scene_image.to_alipay_dict()
            else:
                params['scene_image'] = self.scene_image
        if self.scene_qualification_image:
            if hasattr(self.scene_qualification_image, 'to_alipay_dict'):
                params['scene_qualification_image'] = self.scene_qualification_image.to_alipay_dict()
            else:
                params['scene_qualification_image'] = self.scene_qualification_image
        if self.secondary_partner_info:
            if hasattr(self.secondary_partner_info, 'to_alipay_dict'):
                params['secondary_partner_info'] = self.secondary_partner_info.to_alipay_dict()
            else:
                params['secondary_partner_info'] = self.secondary_partner_info
        if self.sites:
            if hasattr(self.sites, 'to_alipay_dict'):
                params['sites'] = self.sites.to_alipay_dict()
            else:
                params['sites'] = self.sites
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundExpandindirectCreateModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'original_order_id' in d:
            o.original_order_id = d['original_order_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'scene_directions' in d:
            o.scene_directions = d['scene_directions']
        if 'scene_image' in d:
            o.scene_image = d['scene_image']
        if 'scene_qualification_image' in d:
            o.scene_qualification_image = d['scene_qualification_image']
        if 'secondary_partner_info' in d:
            o.secondary_partner_info = d['secondary_partner_info']
        if 'sites' in d:
            o.sites = d['sites']
        return o


