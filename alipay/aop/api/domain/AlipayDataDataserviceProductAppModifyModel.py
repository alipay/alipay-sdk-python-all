#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceProductAppModifyModel(object):

    def __init__(self):
        self._biz_token = None
        self._entity_type = None
        self._out_item_id = None
        self._out_source = None
        self._owner_oid = None
        self._owner_pid = None
        self._principal_tag = None
        self._prod_app_id = None
        self._src_status = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        self._entity_type = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def out_source(self):
        return self._out_source

    @out_source.setter
    def out_source(self, value):
        self._out_source = value
    @property
    def owner_oid(self):
        return self._owner_oid

    @owner_oid.setter
    def owner_oid(self, value):
        self._owner_oid = value
    @property
    def owner_pid(self):
        return self._owner_pid

    @owner_pid.setter
    def owner_pid(self, value):
        self._owner_pid = value
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value
    @property
    def prod_app_id(self):
        return self._prod_app_id

    @prod_app_id.setter
    def prod_app_id(self, value):
        self._prod_app_id = value
    @property
    def src_status(self):
        return self._src_status

    @src_status.setter
    def src_status(self, value):
        self._src_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.entity_type:
            if hasattr(self.entity_type, 'to_alipay_dict'):
                params['entity_type'] = self.entity_type.to_alipay_dict()
            else:
                params['entity_type'] = self.entity_type
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.out_source:
            if hasattr(self.out_source, 'to_alipay_dict'):
                params['out_source'] = self.out_source.to_alipay_dict()
            else:
                params['out_source'] = self.out_source
        if self.owner_oid:
            if hasattr(self.owner_oid, 'to_alipay_dict'):
                params['owner_oid'] = self.owner_oid.to_alipay_dict()
            else:
                params['owner_oid'] = self.owner_oid
        if self.owner_pid:
            if hasattr(self.owner_pid, 'to_alipay_dict'):
                params['owner_pid'] = self.owner_pid.to_alipay_dict()
            else:
                params['owner_pid'] = self.owner_pid
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        if self.prod_app_id:
            if hasattr(self.prod_app_id, 'to_alipay_dict'):
                params['prod_app_id'] = self.prod_app_id.to_alipay_dict()
            else:
                params['prod_app_id'] = self.prod_app_id
        if self.src_status:
            if hasattr(self.src_status, 'to_alipay_dict'):
                params['src_status'] = self.src_status.to_alipay_dict()
            else:
                params['src_status'] = self.src_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceProductAppModifyModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'entity_type' in d:
            o.entity_type = d['entity_type']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'out_source' in d:
            o.out_source = d['out_source']
        if 'owner_oid' in d:
            o.owner_oid = d['owner_oid']
        if 'owner_pid' in d:
            o.owner_pid = d['owner_pid']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'prod_app_id' in d:
            o.prod_app_id = d['prod_app_id']
        if 'src_status' in d:
            o.src_status = d['src_status']
        return o


