#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessRelationChangeMemberInfo import BusinessRelationChangeMemberInfo


class BusinessRelationChangeShopInfo(object):

    def __init__(self):
        self._change_member_infos = None
        self._gmt_create = None
        self._gmt_modified = None
        self._process_status = None
        self._real_shop_id = None
        self._real_shop_no = None
        self._shop_name = None

    @property
    def change_member_infos(self):
        return self._change_member_infos

    @change_member_infos.setter
    def change_member_infos(self, value):
        if isinstance(value, list):
            self._change_member_infos = list()
            for i in value:
                if isinstance(i, BusinessRelationChangeMemberInfo):
                    self._change_member_infos.append(i)
                else:
                    self._change_member_infos.append(BusinessRelationChangeMemberInfo.from_alipay_dict(i))
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def process_status(self):
        return self._process_status

    @process_status.setter
    def process_status(self, value):
        self._process_status = value
    @property
    def real_shop_id(self):
        return self._real_shop_id

    @real_shop_id.setter
    def real_shop_id(self, value):
        self._real_shop_id = value
    @property
    def real_shop_no(self):
        return self._real_shop_no

    @real_shop_no.setter
    def real_shop_no(self, value):
        self._real_shop_no = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.change_member_infos:
            if isinstance(self.change_member_infos, list):
                for i in range(0, len(self.change_member_infos)):
                    element = self.change_member_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.change_member_infos[i] = element.to_alipay_dict()
            if hasattr(self.change_member_infos, 'to_alipay_dict'):
                params['change_member_infos'] = self.change_member_infos.to_alipay_dict()
            else:
                params['change_member_infos'] = self.change_member_infos
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.process_status:
            if hasattr(self.process_status, 'to_alipay_dict'):
                params['process_status'] = self.process_status.to_alipay_dict()
            else:
                params['process_status'] = self.process_status
        if self.real_shop_id:
            if hasattr(self.real_shop_id, 'to_alipay_dict'):
                params['real_shop_id'] = self.real_shop_id.to_alipay_dict()
            else:
                params['real_shop_id'] = self.real_shop_id
        if self.real_shop_no:
            if hasattr(self.real_shop_no, 'to_alipay_dict'):
                params['real_shop_no'] = self.real_shop_no.to_alipay_dict()
            else:
                params['real_shop_no'] = self.real_shop_no
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessRelationChangeShopInfo()
        if 'change_member_infos' in d:
            o.change_member_infos = d['change_member_infos']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'process_status' in d:
            o.process_status = d['process_status']
        if 'real_shop_id' in d:
            o.real_shop_id = d['real_shop_id']
        if 'real_shop_no' in d:
            o.real_shop_no = d['real_shop_no']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        return o


