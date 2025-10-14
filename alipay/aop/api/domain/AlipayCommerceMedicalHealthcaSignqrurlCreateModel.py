#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHealthcaSignqrurlCreateModel(object):

    def __init__(self):
        self._biz_type = None
        self._file_id = None
        self._file_name = None
        self._pos_page = None
        self._pos_x = None
        self._pos_y = None
        self._request_id = None
        self._seal_height = None
        self._seal_width = None
        self._sign_id_card_no = None
        self._sign_name = None
        self._source_url = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def pos_page(self):
        return self._pos_page

    @pos_page.setter
    def pos_page(self, value):
        self._pos_page = value
    @property
    def pos_x(self):
        return self._pos_x

    @pos_x.setter
    def pos_x(self, value):
        self._pos_x = value
    @property
    def pos_y(self):
        return self._pos_y

    @pos_y.setter
    def pos_y(self, value):
        self._pos_y = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def seal_height(self):
        return self._seal_height

    @seal_height.setter
    def seal_height(self, value):
        self._seal_height = value
    @property
    def seal_width(self):
        return self._seal_width

    @seal_width.setter
    def seal_width(self, value):
        self._seal_width = value
    @property
    def sign_id_card_no(self):
        return self._sign_id_card_no

    @sign_id_card_no.setter
    def sign_id_card_no(self, value):
        self._sign_id_card_no = value
    @property
    def sign_name(self):
        return self._sign_name

    @sign_name.setter
    def sign_name(self, value):
        self._sign_name = value
    @property
    def source_url(self):
        return self._source_url

    @source_url.setter
    def source_url(self, value):
        self._source_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.pos_page:
            if hasattr(self.pos_page, 'to_alipay_dict'):
                params['pos_page'] = self.pos_page.to_alipay_dict()
            else:
                params['pos_page'] = self.pos_page
        if self.pos_x:
            if hasattr(self.pos_x, 'to_alipay_dict'):
                params['pos_x'] = self.pos_x.to_alipay_dict()
            else:
                params['pos_x'] = self.pos_x
        if self.pos_y:
            if hasattr(self.pos_y, 'to_alipay_dict'):
                params['pos_y'] = self.pos_y.to_alipay_dict()
            else:
                params['pos_y'] = self.pos_y
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.seal_height:
            if hasattr(self.seal_height, 'to_alipay_dict'):
                params['seal_height'] = self.seal_height.to_alipay_dict()
            else:
                params['seal_height'] = self.seal_height
        if self.seal_width:
            if hasattr(self.seal_width, 'to_alipay_dict'):
                params['seal_width'] = self.seal_width.to_alipay_dict()
            else:
                params['seal_width'] = self.seal_width
        if self.sign_id_card_no:
            if hasattr(self.sign_id_card_no, 'to_alipay_dict'):
                params['sign_id_card_no'] = self.sign_id_card_no.to_alipay_dict()
            else:
                params['sign_id_card_no'] = self.sign_id_card_no
        if self.sign_name:
            if hasattr(self.sign_name, 'to_alipay_dict'):
                params['sign_name'] = self.sign_name.to_alipay_dict()
            else:
                params['sign_name'] = self.sign_name
        if self.source_url:
            if hasattr(self.source_url, 'to_alipay_dict'):
                params['source_url'] = self.source_url.to_alipay_dict()
            else:
                params['source_url'] = self.source_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHealthcaSignqrurlCreateModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'pos_page' in d:
            o.pos_page = d['pos_page']
        if 'pos_x' in d:
            o.pos_x = d['pos_x']
        if 'pos_y' in d:
            o.pos_y = d['pos_y']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'seal_height' in d:
            o.seal_height = d['seal_height']
        if 'seal_width' in d:
            o.seal_width = d['seal_width']
        if 'sign_id_card_no' in d:
            o.sign_id_card_no = d['sign_id_card_no']
        if 'sign_name' in d:
            o.sign_name = d['sign_name']
        if 'source_url' in d:
            o.source_url = d['source_url']
        return o


