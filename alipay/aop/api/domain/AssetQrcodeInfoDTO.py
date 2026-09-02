#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetQrcodeInfoDTO(object):

    def __init__(self):
        self._bind_apply_order_id = None
        self._bind_assign_item_id = None
        self._biz_code = None
        self._biz_no = None
        self._biz_type = None
        self._item_id = None
        self._item_name = None
        self._nfc_url = None
        self._qrcode = None
        self._qrcode_img_url = None
        self._qrcode_url = None
        self._sub_biz_no = None
        self._tag_id = None

    @property
    def bind_apply_order_id(self):
        return self._bind_apply_order_id

    @bind_apply_order_id.setter
    def bind_apply_order_id(self, value):
        self._bind_apply_order_id = value
    @property
    def bind_assign_item_id(self):
        return self._bind_assign_item_id

    @bind_assign_item_id.setter
    def bind_assign_item_id(self, value):
        self._bind_assign_item_id = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def nfc_url(self):
        return self._nfc_url

    @nfc_url.setter
    def nfc_url(self, value):
        self._nfc_url = value
    @property
    def qrcode(self):
        return self._qrcode

    @qrcode.setter
    def qrcode(self, value):
        self._qrcode = value
    @property
    def qrcode_img_url(self):
        return self._qrcode_img_url

    @qrcode_img_url.setter
    def qrcode_img_url(self, value):
        self._qrcode_img_url = value
    @property
    def qrcode_url(self):
        return self._qrcode_url

    @qrcode_url.setter
    def qrcode_url(self, value):
        self._qrcode_url = value
    @property
    def sub_biz_no(self):
        return self._sub_biz_no

    @sub_biz_no.setter
    def sub_biz_no(self, value):
        self._sub_biz_no = value
    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_apply_order_id:
            if hasattr(self.bind_apply_order_id, 'to_alipay_dict'):
                params['bind_apply_order_id'] = self.bind_apply_order_id.to_alipay_dict()
            else:
                params['bind_apply_order_id'] = self.bind_apply_order_id
        if self.bind_assign_item_id:
            if hasattr(self.bind_assign_item_id, 'to_alipay_dict'):
                params['bind_assign_item_id'] = self.bind_assign_item_id.to_alipay_dict()
            else:
                params['bind_assign_item_id'] = self.bind_assign_item_id
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.nfc_url:
            if hasattr(self.nfc_url, 'to_alipay_dict'):
                params['nfc_url'] = self.nfc_url.to_alipay_dict()
            else:
                params['nfc_url'] = self.nfc_url
        if self.qrcode:
            if hasattr(self.qrcode, 'to_alipay_dict'):
                params['qrcode'] = self.qrcode.to_alipay_dict()
            else:
                params['qrcode'] = self.qrcode
        if self.qrcode_img_url:
            if hasattr(self.qrcode_img_url, 'to_alipay_dict'):
                params['qrcode_img_url'] = self.qrcode_img_url.to_alipay_dict()
            else:
                params['qrcode_img_url'] = self.qrcode_img_url
        if self.qrcode_url:
            if hasattr(self.qrcode_url, 'to_alipay_dict'):
                params['qrcode_url'] = self.qrcode_url.to_alipay_dict()
            else:
                params['qrcode_url'] = self.qrcode_url
        if self.sub_biz_no:
            if hasattr(self.sub_biz_no, 'to_alipay_dict'):
                params['sub_biz_no'] = self.sub_biz_no.to_alipay_dict()
            else:
                params['sub_biz_no'] = self.sub_biz_no
        if self.tag_id:
            if hasattr(self.tag_id, 'to_alipay_dict'):
                params['tag_id'] = self.tag_id.to_alipay_dict()
            else:
                params['tag_id'] = self.tag_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetQrcodeInfoDTO()
        if 'bind_apply_order_id' in d:
            o.bind_apply_order_id = d['bind_apply_order_id']
        if 'bind_assign_item_id' in d:
            o.bind_assign_item_id = d['bind_assign_item_id']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'nfc_url' in d:
            o.nfc_url = d['nfc_url']
        if 'qrcode' in d:
            o.qrcode = d['qrcode']
        if 'qrcode_img_url' in d:
            o.qrcode_img_url = d['qrcode_img_url']
        if 'qrcode_url' in d:
            o.qrcode_url = d['qrcode_url']
        if 'sub_biz_no' in d:
            o.sub_biz_no = d['sub_biz_no']
        if 'tag_id' in d:
            o.tag_id = d['tag_id']
        return o


