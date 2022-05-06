#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossBaseFrastressQuerybusinessdomainQueryModel(object):

    def __init__(self):
        self._need_child_domain = None
        self._node_id = None
        self._tnt_inst_id = None
        self._tree_id = None
        self._user_id = None
        self._view = None

    @property
    def need_child_domain(self):
        return self._need_child_domain

    @need_child_domain.setter
    def need_child_domain(self, value):
        self._need_child_domain = value
    @property
    def node_id(self):
        return self._node_id

    @node_id.setter
    def node_id(self, value):
        self._node_id = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def tree_id(self):
        return self._tree_id

    @tree_id.setter
    def tree_id(self, value):
        self._tree_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def view(self):
        return self._view

    @view.setter
    def view(self, value):
        self._view = value


    def to_alipay_dict(self):
        params = dict()
        if self.need_child_domain:
            if hasattr(self.need_child_domain, 'to_alipay_dict'):
                params['need_child_domain'] = self.need_child_domain.to_alipay_dict()
            else:
                params['need_child_domain'] = self.need_child_domain
        if self.node_id:
            if hasattr(self.node_id, 'to_alipay_dict'):
                params['node_id'] = self.node_id.to_alipay_dict()
            else:
                params['node_id'] = self.node_id
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        if self.tree_id:
            if hasattr(self.tree_id, 'to_alipay_dict'):
                params['tree_id'] = self.tree_id.to_alipay_dict()
            else:
                params['tree_id'] = self.tree_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.view:
            if hasattr(self.view, 'to_alipay_dict'):
                params['view'] = self.view.to_alipay_dict()
            else:
                params['view'] = self.view
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossBaseFrastressQuerybusinessdomainQueryModel()
        if 'need_child_domain' in d:
            o.need_child_domain = d['need_child_domain']
        if 'node_id' in d:
            o.node_id = d['node_id']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'tree_id' in d:
            o.tree_id = d['tree_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'view' in d:
            o.view = d['view']
        return o


