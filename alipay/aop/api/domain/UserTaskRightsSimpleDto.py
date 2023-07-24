#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserTaskRightsSimpleDto(object):

    def __init__(self):
        self._award_count = None
        self._ext_info = None
        self._gmt_receive = None
        self._out_biz_no = None
        self._receive_deadline = None
        self._rights_id = None
        self._rights_name = None
        self._rights_type = None
        self._status = None
        self._user_task_rights_id = None

    @property
    def award_count(self):
        return self._award_count

    @award_count.setter
    def award_count(self, value):
        self._award_count = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def gmt_receive(self):
        return self._gmt_receive

    @gmt_receive.setter
    def gmt_receive(self, value):
        self._gmt_receive = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def receive_deadline(self):
        return self._receive_deadline

    @receive_deadline.setter
    def receive_deadline(self, value):
        self._receive_deadline = value
    @property
    def rights_id(self):
        return self._rights_id

    @rights_id.setter
    def rights_id(self, value):
        self._rights_id = value
    @property
    def rights_name(self):
        return self._rights_name

    @rights_name.setter
    def rights_name(self, value):
        self._rights_name = value
    @property
    def rights_type(self):
        return self._rights_type

    @rights_type.setter
    def rights_type(self, value):
        self._rights_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_task_rights_id(self):
        return self._user_task_rights_id

    @user_task_rights_id.setter
    def user_task_rights_id(self, value):
        self._user_task_rights_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.award_count:
            if hasattr(self.award_count, 'to_alipay_dict'):
                params['award_count'] = self.award_count.to_alipay_dict()
            else:
                params['award_count'] = self.award_count
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.gmt_receive:
            if hasattr(self.gmt_receive, 'to_alipay_dict'):
                params['gmt_receive'] = self.gmt_receive.to_alipay_dict()
            else:
                params['gmt_receive'] = self.gmt_receive
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.receive_deadline:
            if hasattr(self.receive_deadline, 'to_alipay_dict'):
                params['receive_deadline'] = self.receive_deadline.to_alipay_dict()
            else:
                params['receive_deadline'] = self.receive_deadline
        if self.rights_id:
            if hasattr(self.rights_id, 'to_alipay_dict'):
                params['rights_id'] = self.rights_id.to_alipay_dict()
            else:
                params['rights_id'] = self.rights_id
        if self.rights_name:
            if hasattr(self.rights_name, 'to_alipay_dict'):
                params['rights_name'] = self.rights_name.to_alipay_dict()
            else:
                params['rights_name'] = self.rights_name
        if self.rights_type:
            if hasattr(self.rights_type, 'to_alipay_dict'):
                params['rights_type'] = self.rights_type.to_alipay_dict()
            else:
                params['rights_type'] = self.rights_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.user_task_rights_id:
            if hasattr(self.user_task_rights_id, 'to_alipay_dict'):
                params['user_task_rights_id'] = self.user_task_rights_id.to_alipay_dict()
            else:
                params['user_task_rights_id'] = self.user_task_rights_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserTaskRightsSimpleDto()
        if 'award_count' in d:
            o.award_count = d['award_count']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gmt_receive' in d:
            o.gmt_receive = d['gmt_receive']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'receive_deadline' in d:
            o.receive_deadline = d['receive_deadline']
        if 'rights_id' in d:
            o.rights_id = d['rights_id']
        if 'rights_name' in d:
            o.rights_name = d['rights_name']
        if 'rights_type' in d:
            o.rights_type = d['rights_type']
        if 'status' in d:
            o.status = d['status']
        if 'user_task_rights_id' in d:
            o.user_task_rights_id = d['user_task_rights_id']
        return o


