#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandDeliveryGoodsinfoSyncModel(object):

    def __init__(self):
        self._assign_item_id = None
        self._ext_info = None
        self._logistics_no = None
        self._send_goods_tag = None
        self._tag_type = None

    @property
    def assign_item_id(self):
        return self._assign_item_id

    @assign_item_id.setter
    def assign_item_id(self, value):
        self._assign_item_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def logistics_no(self):
        return self._logistics_no

    @logistics_no.setter
    def logistics_no(self, value):
        self._logistics_no = value
    @property
    def send_goods_tag(self):
        return self._send_goods_tag

    @send_goods_tag.setter
    def send_goods_tag(self, value):
        self._send_goods_tag = value
    @property
    def tag_type(self):
        return self._tag_type

    @tag_type.setter
    def tag_type(self, value):
        self._tag_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.assign_item_id:
            if hasattr(self.assign_item_id, 'to_alipay_dict'):
                params['assign_item_id'] = self.assign_item_id.to_alipay_dict()
            else:
                params['assign_item_id'] = self.assign_item_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.logistics_no:
            if hasattr(self.logistics_no, 'to_alipay_dict'):
                params['logistics_no'] = self.logistics_no.to_alipay_dict()
            else:
                params['logistics_no'] = self.logistics_no
        if self.send_goods_tag:
            if hasattr(self.send_goods_tag, 'to_alipay_dict'):
                params['send_goods_tag'] = self.send_goods_tag.to_alipay_dict()
            else:
                params['send_goods_tag'] = self.send_goods_tag
        if self.tag_type:
            if hasattr(self.tag_type, 'to_alipay_dict'):
                params['tag_type'] = self.tag_type.to_alipay_dict()
            else:
                params['tag_type'] = self.tag_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandDeliveryGoodsinfoSyncModel()
        if 'assign_item_id' in d:
            o.assign_item_id = d['assign_item_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'logistics_no' in d:
            o.logistics_no = d['logistics_no']
        if 'send_goods_tag' in d:
            o.send_goods_tag = d['send_goods_tag']
        if 'tag_type' in d:
            o.tag_type = d['tag_type']
        return o


