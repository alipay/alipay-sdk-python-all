#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SquareDanceTaskInfo(object):

    def __init__(self):
        self._application_id = None
        self._biz_type = None
        self._button_action_url = None
        self._button_text = None
        self._ext_info = None
        self._flow_id = None
        self._img_url = None
        self._status = None
        self._sub_title = None
        self._task_id = None
        self._title = None
        self._votes = None

    @property
    def application_id(self):
        return self._application_id

    @application_id.setter
    def application_id(self, value):
        self._application_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def button_action_url(self):
        return self._button_action_url

    @button_action_url.setter
    def button_action_url(self, value):
        self._button_action_url = value
    @property
    def button_text(self):
        return self._button_text

    @button_text.setter
    def button_text(self, value):
        self._button_text = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def flow_id(self):
        return self._flow_id

    @flow_id.setter
    def flow_id(self, value):
        self._flow_id = value
    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def votes(self):
        return self._votes

    @votes.setter
    def votes(self, value):
        self._votes = value


    def to_alipay_dict(self):
        params = dict()
        if self.application_id:
            if hasattr(self.application_id, 'to_alipay_dict'):
                params['application_id'] = self.application_id.to_alipay_dict()
            else:
                params['application_id'] = self.application_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.button_action_url:
            if hasattr(self.button_action_url, 'to_alipay_dict'):
                params['button_action_url'] = self.button_action_url.to_alipay_dict()
            else:
                params['button_action_url'] = self.button_action_url
        if self.button_text:
            if hasattr(self.button_text, 'to_alipay_dict'):
                params['button_text'] = self.button_text.to_alipay_dict()
            else:
                params['button_text'] = self.button_text
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.flow_id:
            if hasattr(self.flow_id, 'to_alipay_dict'):
                params['flow_id'] = self.flow_id.to_alipay_dict()
            else:
                params['flow_id'] = self.flow_id
        if self.img_url:
            if hasattr(self.img_url, 'to_alipay_dict'):
                params['img_url'] = self.img_url.to_alipay_dict()
            else:
                params['img_url'] = self.img_url
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_title:
            if hasattr(self.sub_title, 'to_alipay_dict'):
                params['sub_title'] = self.sub_title.to_alipay_dict()
            else:
                params['sub_title'] = self.sub_title
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.votes:
            if hasattr(self.votes, 'to_alipay_dict'):
                params['votes'] = self.votes.to_alipay_dict()
            else:
                params['votes'] = self.votes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SquareDanceTaskInfo()
        if 'application_id' in d:
            o.application_id = d['application_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'button_action_url' in d:
            o.button_action_url = d['button_action_url']
        if 'button_text' in d:
            o.button_text = d['button_text']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'flow_id' in d:
            o.flow_id = d['flow_id']
        if 'img_url' in d:
            o.img_url = d['img_url']
        if 'status' in d:
            o.status = d['status']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'title' in d:
            o.title = d['title']
        if 'votes' in d:
            o.votes = d['votes']
        return o


