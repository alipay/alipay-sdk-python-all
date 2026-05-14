#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftSkuCastSubmitModel(object):

    def __init__(self):
        self._apply_no = None
        self._author = None
        self._creation_time = None
        self._custom_flag = None
        self._issuer = None
        self._quantity = None
        self._sku_ac_color = None
        self._sku_class = None
        self._sku_introduction = None
        self._sku_name = None
        self._sku_type = None
        self._source_file_model_id = None
        self._sub_sku_class = None
        self._thumbnail_model_id = None
        self._unlimited_ac_code = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value
    @property
    def creation_time(self):
        return self._creation_time

    @creation_time.setter
    def creation_time(self, value):
        self._creation_time = value
    @property
    def custom_flag(self):
        return self._custom_flag

    @custom_flag.setter
    def custom_flag(self, value):
        self._custom_flag = value
    @property
    def issuer(self):
        return self._issuer

    @issuer.setter
    def issuer(self, value):
        self._issuer = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def sku_ac_color(self):
        return self._sku_ac_color

    @sku_ac_color.setter
    def sku_ac_color(self, value):
        self._sku_ac_color = value
    @property
    def sku_class(self):
        return self._sku_class

    @sku_class.setter
    def sku_class(self, value):
        self._sku_class = value
    @property
    def sku_introduction(self):
        return self._sku_introduction

    @sku_introduction.setter
    def sku_introduction(self, value):
        self._sku_introduction = value
    @property
    def sku_name(self):
        return self._sku_name

    @sku_name.setter
    def sku_name(self, value):
        self._sku_name = value
    @property
    def sku_type(self):
        return self._sku_type

    @sku_type.setter
    def sku_type(self, value):
        self._sku_type = value
    @property
    def source_file_model_id(self):
        return self._source_file_model_id

    @source_file_model_id.setter
    def source_file_model_id(self, value):
        self._source_file_model_id = value
    @property
    def sub_sku_class(self):
        return self._sub_sku_class

    @sub_sku_class.setter
    def sub_sku_class(self, value):
        self._sub_sku_class = value
    @property
    def thumbnail_model_id(self):
        return self._thumbnail_model_id

    @thumbnail_model_id.setter
    def thumbnail_model_id(self, value):
        self._thumbnail_model_id = value
    @property
    def unlimited_ac_code(self):
        return self._unlimited_ac_code

    @unlimited_ac_code.setter
    def unlimited_ac_code(self, value):
        self._unlimited_ac_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.author:
            if hasattr(self.author, 'to_alipay_dict'):
                params['author'] = self.author.to_alipay_dict()
            else:
                params['author'] = self.author
        if self.creation_time:
            if hasattr(self.creation_time, 'to_alipay_dict'):
                params['creation_time'] = self.creation_time.to_alipay_dict()
            else:
                params['creation_time'] = self.creation_time
        if self.custom_flag:
            if hasattr(self.custom_flag, 'to_alipay_dict'):
                params['custom_flag'] = self.custom_flag.to_alipay_dict()
            else:
                params['custom_flag'] = self.custom_flag
        if self.issuer:
            if hasattr(self.issuer, 'to_alipay_dict'):
                params['issuer'] = self.issuer.to_alipay_dict()
            else:
                params['issuer'] = self.issuer
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.sku_ac_color:
            if hasattr(self.sku_ac_color, 'to_alipay_dict'):
                params['sku_ac_color'] = self.sku_ac_color.to_alipay_dict()
            else:
                params['sku_ac_color'] = self.sku_ac_color
        if self.sku_class:
            if hasattr(self.sku_class, 'to_alipay_dict'):
                params['sku_class'] = self.sku_class.to_alipay_dict()
            else:
                params['sku_class'] = self.sku_class
        if self.sku_introduction:
            if hasattr(self.sku_introduction, 'to_alipay_dict'):
                params['sku_introduction'] = self.sku_introduction.to_alipay_dict()
            else:
                params['sku_introduction'] = self.sku_introduction
        if self.sku_name:
            if hasattr(self.sku_name, 'to_alipay_dict'):
                params['sku_name'] = self.sku_name.to_alipay_dict()
            else:
                params['sku_name'] = self.sku_name
        if self.sku_type:
            if hasattr(self.sku_type, 'to_alipay_dict'):
                params['sku_type'] = self.sku_type.to_alipay_dict()
            else:
                params['sku_type'] = self.sku_type
        if self.source_file_model_id:
            if hasattr(self.source_file_model_id, 'to_alipay_dict'):
                params['source_file_model_id'] = self.source_file_model_id.to_alipay_dict()
            else:
                params['source_file_model_id'] = self.source_file_model_id
        if self.sub_sku_class:
            if hasattr(self.sub_sku_class, 'to_alipay_dict'):
                params['sub_sku_class'] = self.sub_sku_class.to_alipay_dict()
            else:
                params['sub_sku_class'] = self.sub_sku_class
        if self.thumbnail_model_id:
            if hasattr(self.thumbnail_model_id, 'to_alipay_dict'):
                params['thumbnail_model_id'] = self.thumbnail_model_id.to_alipay_dict()
            else:
                params['thumbnail_model_id'] = self.thumbnail_model_id
        if self.unlimited_ac_code:
            if hasattr(self.unlimited_ac_code, 'to_alipay_dict'):
                params['unlimited_ac_code'] = self.unlimited_ac_code.to_alipay_dict()
            else:
                params['unlimited_ac_code'] = self.unlimited_ac_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftSkuCastSubmitModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'author' in d:
            o.author = d['author']
        if 'creation_time' in d:
            o.creation_time = d['creation_time']
        if 'custom_flag' in d:
            o.custom_flag = d['custom_flag']
        if 'issuer' in d:
            o.issuer = d['issuer']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'sku_ac_color' in d:
            o.sku_ac_color = d['sku_ac_color']
        if 'sku_class' in d:
            o.sku_class = d['sku_class']
        if 'sku_introduction' in d:
            o.sku_introduction = d['sku_introduction']
        if 'sku_name' in d:
            o.sku_name = d['sku_name']
        if 'sku_type' in d:
            o.sku_type = d['sku_type']
        if 'source_file_model_id' in d:
            o.source_file_model_id = d['source_file_model_id']
        if 'sub_sku_class' in d:
            o.sub_sku_class = d['sub_sku_class']
        if 'thumbnail_model_id' in d:
            o.thumbnail_model_id = d['thumbnail_model_id']
        if 'unlimited_ac_code' in d:
            o.unlimited_ac_code = d['unlimited_ac_code']
        return o


