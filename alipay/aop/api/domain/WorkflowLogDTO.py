#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PersonDTO import PersonDTO
from alipay.aop.api.domain.FileDTO import FileDTO


class WorkflowLogDTO(object):

    def __init__(self):
        self._approval_role = None
        self._approve_time = None
        self._approver = None
        self._attachments = None
        self._comments = None
        self._operation = None

    @property
    def approval_role(self):
        return self._approval_role

    @approval_role.setter
    def approval_role(self, value):
        self._approval_role = value
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
        if isinstance(value, PersonDTO):
            self._approver = value
        else:
            self._approver = PersonDTO.from_alipay_dict(value)
    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        if isinstance(value, list):
            self._attachments = list()
            for i in value:
                if isinstance(i, FileDTO):
                    self._attachments.append(i)
                else:
                    self._attachments.append(FileDTO.from_alipay_dict(i))
    @property
    def comments(self):
        return self._comments

    @comments.setter
    def comments(self, value):
        self._comments = value
    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, value):
        self._operation = value


    def to_alipay_dict(self):
        params = dict()
        if self.approval_role:
            if hasattr(self.approval_role, 'to_alipay_dict'):
                params['approval_role'] = self.approval_role.to_alipay_dict()
            else:
                params['approval_role'] = self.approval_role
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
        if self.attachments:
            if isinstance(self.attachments, list):
                for i in range(0, len(self.attachments)):
                    element = self.attachments[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachments[i] = element.to_alipay_dict()
            if hasattr(self.attachments, 'to_alipay_dict'):
                params['attachments'] = self.attachments.to_alipay_dict()
            else:
                params['attachments'] = self.attachments
        if self.comments:
            if hasattr(self.comments, 'to_alipay_dict'):
                params['comments'] = self.comments.to_alipay_dict()
            else:
                params['comments'] = self.comments
        if self.operation:
            if hasattr(self.operation, 'to_alipay_dict'):
                params['operation'] = self.operation.to_alipay_dict()
            else:
                params['operation'] = self.operation
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WorkflowLogDTO()
        if 'approval_role' in d:
            o.approval_role = d['approval_role']
        if 'approve_time' in d:
            o.approve_time = d['approve_time']
        if 'approver' in d:
            o.approver = d['approver']
        if 'attachments' in d:
            o.attachments = d['attachments']
        if 'comments' in d:
            o.comments = d['comments']
        if 'operation' in d:
            o.operation = d['operation']
        return o


