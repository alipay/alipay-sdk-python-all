#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SpuAttributeInfoVO import SpuAttributeInfoVO
from alipay.aop.api.domain.SpuAttributeInfoVO import SpuAttributeInfoVO


class SpuInfoVO(object):

    def __init__(self):
        self._bind_attrs = None
        self._category_id = None
        self._key_attrs = None
        self._pic_urls = None
        self._spu_id = None
        self._spu_name = None
        self._status = None

    @property
    def bind_attrs(self):
        return self._bind_attrs

    @bind_attrs.setter
    def bind_attrs(self, value):
        if isinstance(value, list):
            self._bind_attrs = list()
            for i in value:
                if isinstance(i, SpuAttributeInfoVO):
                    self._bind_attrs.append(i)
                else:
                    self._bind_attrs.append(SpuAttributeInfoVO.from_alipay_dict(i))
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def key_attrs(self):
        return self._key_attrs

    @key_attrs.setter
    def key_attrs(self, value):
        if isinstance(value, list):
            self._key_attrs = list()
            for i in value:
                if isinstance(i, SpuAttributeInfoVO):
                    self._key_attrs.append(i)
                else:
                    self._key_attrs.append(SpuAttributeInfoVO.from_alipay_dict(i))
    @property
    def pic_urls(self):
        return self._pic_urls

    @pic_urls.setter
    def pic_urls(self, value):
        if isinstance(value, list):
            self._pic_urls = list()
            for i in value:
                self._pic_urls.append(i)
    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, value):
        self._spu_id = value
    @property
    def spu_name(self):
        return self._spu_name

    @spu_name.setter
    def spu_name(self, value):
        self._spu_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_attrs:
            if isinstance(self.bind_attrs, list):
                for i in range(0, len(self.bind_attrs)):
                    element = self.bind_attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bind_attrs[i] = element.to_alipay_dict()
            if hasattr(self.bind_attrs, 'to_alipay_dict'):
                params['bind_attrs'] = self.bind_attrs.to_alipay_dict()
            else:
                params['bind_attrs'] = self.bind_attrs
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.key_attrs:
            if isinstance(self.key_attrs, list):
                for i in range(0, len(self.key_attrs)):
                    element = self.key_attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.key_attrs[i] = element.to_alipay_dict()
            if hasattr(self.key_attrs, 'to_alipay_dict'):
                params['key_attrs'] = self.key_attrs.to_alipay_dict()
            else:
                params['key_attrs'] = self.key_attrs
        if self.pic_urls:
            if isinstance(self.pic_urls, list):
                for i in range(0, len(self.pic_urls)):
                    element = self.pic_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pic_urls[i] = element.to_alipay_dict()
            if hasattr(self.pic_urls, 'to_alipay_dict'):
                params['pic_urls'] = self.pic_urls.to_alipay_dict()
            else:
                params['pic_urls'] = self.pic_urls
        if self.spu_id:
            if hasattr(self.spu_id, 'to_alipay_dict'):
                params['spu_id'] = self.spu_id.to_alipay_dict()
            else:
                params['spu_id'] = self.spu_id
        if self.spu_name:
            if hasattr(self.spu_name, 'to_alipay_dict'):
                params['spu_name'] = self.spu_name.to_alipay_dict()
            else:
                params['spu_name'] = self.spu_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpuInfoVO()
        if 'bind_attrs' in d:
            o.bind_attrs = d['bind_attrs']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'key_attrs' in d:
            o.key_attrs = d['key_attrs']
        if 'pic_urls' in d:
            o.pic_urls = d['pic_urls']
        if 'spu_id' in d:
            o.spu_id = d['spu_id']
        if 'spu_name' in d:
            o.spu_name = d['spu_name']
        if 'status' in d:
            o.status = d['status']
        return o


