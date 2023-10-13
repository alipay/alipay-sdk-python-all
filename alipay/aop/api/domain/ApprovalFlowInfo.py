#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreateESignTaskFileVO import CreateESignTaskFileVO


class ApprovalFlowInfo(object):

    def __init__(self):
        self._approve_status = None
        self._approve_time = None
        self._approver = None
        self._approver_name = None
        self._approver_nick_name = None
        self._attachement_list = None
        self._comments = None
        self._index = None
        self._node = None

    @property
    def approve_status(self):
        return self._approve_status

    @approve_status.setter
    def approve_status(self, value):
        self._approve_status = value
    @property
    def approve_time(self):
        return self._approve_time

    @approve_time.setter
    def approve_time(self, value):
        self._approve_time = value
    @property
    def approver(self):
        return self._approver

    @approver.setter
    def approver(self, value):
        self._approver = value
    @property
    def approver_name(self):
        return self._approver_name

    @approver_name.setter
    def approver_name(self, value):
        self._approver_name = value
    @property
    def approver_nick_name(self):
        return self._approver_nick_name

    @approver_nick_name.setter
    def approver_nick_name(self, value):
        self._approver_nick_name = value
    @property
    def attachement_list(self):
        return self._attachement_list

    @attachement_list.setter
    def attachement_list(self, value):
        if isinstance(value, list):
            self._attachement_list = list()
            for i in value:
                if isinstance(i, CreateESignTaskFileVO):
                    self._attachement_list.append(i)
                else:
                    self._attachement_list.append(CreateESignTaskFileVO.from_alipay_dict(i))
    @property
    def comments(self):
        return self._comments

    @comments.setter
    def comments(self, value):
        self._comments = value
    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value
    @property
    def node(self):
        return self._node

    @node.setter
    def node(self, value):
        self._node = value


    def to_alipay_dict(self):
        params = dict()
        if self.approve_status:
            if hasattr(self.approve_status, 'to_alipay_dict'):
                params['approve_status'] = self.approve_status.to_alipay_dict()
            else:
                params['approve_status'] = self.approve_status
        if self.approve_time:
            if hasattr(self.approve_time, 'to_alipay_dict'):
                params['approve_time'] = self.approve_time.to_alipay_dict()
            else:
                params['approve_time'] = self.approve_time
        if self.approver:
            if hasattr(self.approver, 'to_alipay_dict'):
                params['approver'] = self.approver.to_alipay_dict()
            else:
                params['approver'] = self.approver
        if self.approver_name:
            if hasattr(self.approver_name, 'to_alipay_dict'):
                params['approver_name'] = self.approver_name.to_alipay_dict()
            else:
                params['approver_name'] = self.approver_name
        if self.approver_nick_name:
            if hasattr(self.approver_nick_name, 'to_alipay_dict'):
                params['approver_nick_name'] = self.approver_nick_name.to_alipay_dict()
            else:
                params['approver_nick_name'] = self.approver_nick_name
        if self.attachement_list:
            if isinstance(self.attachement_list, list):
                for i in range(0, len(self.attachement_list)):
                    element = self.attachement_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachement_list[i] = element.to_alipay_dict()
            if hasattr(self.attachement_list, 'to_alipay_dict'):
                params['attachement_list'] = self.attachement_list.to_alipay_dict()
            else:
                params['attachement_list'] = self.attachement_list
        if self.comments:
            if hasattr(self.comments, 'to_alipay_dict'):
                params['comments'] = self.comments.to_alipay_dict()
            else:
                params['comments'] = self.comments
        if self.index:
            if hasattr(self.index, 'to_alipay_dict'):
                params['index'] = self.index.to_alipay_dict()
            else:
                params['index'] = self.index
        if self.node:
            if hasattr(self.node, 'to_alipay_dict'):
                params['node'] = self.node.to_alipay_dict()
            else:
                params['node'] = self.node
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApprovalFlowInfo()
        if 'approve_status' in d:
            o.approve_status = d['approve_status']
        if 'approve_time' in d:
            o.approve_time = d['approve_time']
        if 'approver' in d:
            o.approver = d['approver']
        if 'approver_name' in d:
            o.approver_name = d['approver_name']
        if 'approver_nick_name' in d:
            o.approver_nick_name = d['approver_nick_name']
        if 'attachement_list' in d:
            o.attachement_list = d['attachement_list']
        if 'comments' in d:
            o.comments = d['comments']
        if 'index' in d:
            o.index = d['index']
        if 'node' in d:
            o.node = d['node']
        return o


