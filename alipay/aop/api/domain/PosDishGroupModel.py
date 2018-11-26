#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PosDishGroupDetailModel import PosDishGroupDetailModel
from alipay.aop.api.domain.PosDishGroupDetailModel import PosDishGroupDetailModel


class PosDishGroupModel(object):

    def __init__(self):
        self._create_user = None
        self._detail_list = None
        self._group_id = None
        self._group_name = None
        self._query_detail_list = None
        self._shop_id = None
        self._sort = None
        self._status = None
        self._sync_type = None
        self._unit_count_limit = None
        self._update_user = None

    @property
    def create_user(self):
        return self._create_user

    @create_user.setter
    def create_user(self, value):
        self._create_user = value
    @property
    def detail_list(self):
        return self._detail_list

    @detail_list.setter
    def detail_list(self, value):
        if isinstance(value, list):
            self._detail_list = list()
            for i in value:
                if isinstance(i, PosDishGroupDetailModel):
                    self._detail_list.append(i)
                else:
                    self._detail_list.append(PosDishGroupDetailModel.from_alipay_dict(i))
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def query_detail_list(self):
        return self._query_detail_list

    @query_detail_list.setter
    def query_detail_list(self, value):
        if isinstance(value, list):
            self._query_detail_list = list()
            for i in value:
                if isinstance(i, PosDishGroupDetailModel):
                    self._query_detail_list.append(i)
                else:
                    self._query_detail_list.append(PosDishGroupDetailModel.from_alipay_dict(i))
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sync_type(self):
        return self._sync_type

    @sync_type.setter
    def sync_type(self, value):
        self._sync_type = value
    @property
    def unit_count_limit(self):
        return self._unit_count_limit

    @unit_count_limit.setter
    def unit_count_limit(self, value):
        self._unit_count_limit = value
    @property
    def update_user(self):
        return self._update_user

    @update_user.setter
    def update_user(self, value):
        self._update_user = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_user:
            if hasattr(self.create_user, 'to_alipay_dict'):
                params['create_user'] = self.create_user.to_alipay_dict()
            else:
                params['create_user'] = self.create_user
        if self.detail_list:
            if isinstance(self.detail_list, list):
                for i in range(0, len(self.detail_list)):
                    element = self.detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.detail_list[i] = element.to_alipay_dict()
            if hasattr(self.detail_list, 'to_alipay_dict'):
                params['detail_list'] = self.detail_list.to_alipay_dict()
            else:
                params['detail_list'] = self.detail_list
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.query_detail_list:
            if isinstance(self.query_detail_list, list):
                for i in range(0, len(self.query_detail_list)):
                    element = self.query_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.query_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.query_detail_list, 'to_alipay_dict'):
                params['query_detail_list'] = self.query_detail_list.to_alipay_dict()
            else:
                params['query_detail_list'] = self.query_detail_list
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sync_type:
            if hasattr(self.sync_type, 'to_alipay_dict'):
                params['sync_type'] = self.sync_type.to_alipay_dict()
            else:
                params['sync_type'] = self.sync_type
        if self.unit_count_limit:
            if hasattr(self.unit_count_limit, 'to_alipay_dict'):
                params['unit_count_limit'] = self.unit_count_limit.to_alipay_dict()
            else:
                params['unit_count_limit'] = self.unit_count_limit
        if self.update_user:
            if hasattr(self.update_user, 'to_alipay_dict'):
                params['update_user'] = self.update_user.to_alipay_dict()
            else:
                params['update_user'] = self.update_user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PosDishGroupModel()
        if 'create_user' in d:
            o.create_user = d['create_user']
        if 'detail_list' in d:
            o.detail_list = d['detail_list']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'query_detail_list' in d:
            o.query_detail_list = d['query_detail_list']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sort' in d:
            o.sort = d['sort']
        if 'status' in d:
            o.status = d['status']
        if 'sync_type' in d:
            o.sync_type = d['sync_type']
        if 'unit_count_limit' in d:
            o.unit_count_limit = d['unit_count_limit']
        if 'update_user' in d:
            o.update_user = d['update_user']
        return o


