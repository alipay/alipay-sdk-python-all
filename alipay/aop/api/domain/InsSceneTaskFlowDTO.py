#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsSceneTaskFlowDTO(object):

    def __init__(self):
        self._expired_time = None
        self._extra_map = None
        self._finish_time = None
        self._gmt_create = None
        self._gmt_modified = None
        self._join_id = None
        self._marketing_scene = None
        self._out_biz_no = None
        self._participant_user_id = None
        self._participator_user_id = None
        self._receive_time = None
        self._status = None
        self._task_flowid = None
        self._type = None

    @property
    def expired_time(self):
        return self._expired_time

    @expired_time.setter
    def expired_time(self, value):
        self._expired_time = value
    @property
    def extra_map(self):
        return self._extra_map

    @extra_map.setter
    def extra_map(self, value):
        self._extra_map = value
    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
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
    def join_id(self):
        return self._join_id

    @join_id.setter
    def join_id(self, value):
        self._join_id = value
    @property
    def marketing_scene(self):
        return self._marketing_scene

    @marketing_scene.setter
    def marketing_scene(self, value):
        self._marketing_scene = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def participant_user_id(self):
        return self._participant_user_id

    @participant_user_id.setter
    def participant_user_id(self, value):
        self._participant_user_id = value
    @property
    def participator_user_id(self):
        return self._participator_user_id

    @participator_user_id.setter
    def participator_user_id(self, value):
        self._participator_user_id = value
    @property
    def receive_time(self):
        return self._receive_time

    @receive_time.setter
    def receive_time(self, value):
        self._receive_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_flowid(self):
        return self._task_flowid

    @task_flowid.setter
    def task_flowid(self, value):
        self._task_flowid = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.expired_time:
            if hasattr(self.expired_time, 'to_alipay_dict'):
                params['expired_time'] = self.expired_time.to_alipay_dict()
            else:
                params['expired_time'] = self.expired_time
        if self.extra_map:
            if hasattr(self.extra_map, 'to_alipay_dict'):
                params['extra_map'] = self.extra_map.to_alipay_dict()
            else:
                params['extra_map'] = self.extra_map
        if self.finish_time:
            if hasattr(self.finish_time, 'to_alipay_dict'):
                params['finish_time'] = self.finish_time.to_alipay_dict()
            else:
                params['finish_time'] = self.finish_time
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
        if self.join_id:
            if hasattr(self.join_id, 'to_alipay_dict'):
                params['join_id'] = self.join_id.to_alipay_dict()
            else:
                params['join_id'] = self.join_id
        if self.marketing_scene:
            if hasattr(self.marketing_scene, 'to_alipay_dict'):
                params['marketing_scene'] = self.marketing_scene.to_alipay_dict()
            else:
                params['marketing_scene'] = self.marketing_scene
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.participant_user_id:
            if hasattr(self.participant_user_id, 'to_alipay_dict'):
                params['participant_user_id'] = self.participant_user_id.to_alipay_dict()
            else:
                params['participant_user_id'] = self.participant_user_id
        if self.participator_user_id:
            if hasattr(self.participator_user_id, 'to_alipay_dict'):
                params['participator_user_id'] = self.participator_user_id.to_alipay_dict()
            else:
                params['participator_user_id'] = self.participator_user_id
        if self.receive_time:
            if hasattr(self.receive_time, 'to_alipay_dict'):
                params['receive_time'] = self.receive_time.to_alipay_dict()
            else:
                params['receive_time'] = self.receive_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.task_flowid:
            if hasattr(self.task_flowid, 'to_alipay_dict'):
                params['task_flowid'] = self.task_flowid.to_alipay_dict()
            else:
                params['task_flowid'] = self.task_flowid
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsSceneTaskFlowDTO()
        if 'expired_time' in d:
            o.expired_time = d['expired_time']
        if 'extra_map' in d:
            o.extra_map = d['extra_map']
        if 'finish_time' in d:
            o.finish_time = d['finish_time']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'join_id' in d:
            o.join_id = d['join_id']
        if 'marketing_scene' in d:
            o.marketing_scene = d['marketing_scene']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'participant_user_id' in d:
            o.participant_user_id = d['participant_user_id']
        if 'participator_user_id' in d:
            o.participator_user_id = d['participator_user_id']
        if 'receive_time' in d:
            o.receive_time = d['receive_time']
        if 'status' in d:
            o.status = d['status']
        if 'task_flowid' in d:
            o.task_flowid = d['task_flowid']
        if 'type' in d:
            o.type = d['type']
        return o


