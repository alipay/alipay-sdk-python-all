#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CorpusPublishTaskResult(object):

    def __init__(self):
        self._corpus_type = None
        self._create_time = None
        self._process_success_count = None
        self._process_total_count = None
        self._publish_name = None
        self._publish_type = None
        self._task_status = None

    @property
    def corpus_type(self):
        return self._corpus_type

    @corpus_type.setter
    def corpus_type(self, value):
        self._corpus_type = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def process_success_count(self):
        return self._process_success_count

    @process_success_count.setter
    def process_success_count(self, value):
        self._process_success_count = value
    @property
    def process_total_count(self):
        return self._process_total_count

    @process_total_count.setter
    def process_total_count(self, value):
        self._process_total_count = value
    @property
    def publish_name(self):
        return self._publish_name

    @publish_name.setter
    def publish_name(self, value):
        self._publish_name = value
    @property
    def publish_type(self):
        return self._publish_type

    @publish_type.setter
    def publish_type(self, value):
        self._publish_type = value
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.corpus_type:
            if hasattr(self.corpus_type, 'to_alipay_dict'):
                params['corpus_type'] = self.corpus_type.to_alipay_dict()
            else:
                params['corpus_type'] = self.corpus_type
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.process_success_count:
            if hasattr(self.process_success_count, 'to_alipay_dict'):
                params['process_success_count'] = self.process_success_count.to_alipay_dict()
            else:
                params['process_success_count'] = self.process_success_count
        if self.process_total_count:
            if hasattr(self.process_total_count, 'to_alipay_dict'):
                params['process_total_count'] = self.process_total_count.to_alipay_dict()
            else:
                params['process_total_count'] = self.process_total_count
        if self.publish_name:
            if hasattr(self.publish_name, 'to_alipay_dict'):
                params['publish_name'] = self.publish_name.to_alipay_dict()
            else:
                params['publish_name'] = self.publish_name
        if self.publish_type:
            if hasattr(self.publish_type, 'to_alipay_dict'):
                params['publish_type'] = self.publish_type.to_alipay_dict()
            else:
                params['publish_type'] = self.publish_type
        if self.task_status:
            if hasattr(self.task_status, 'to_alipay_dict'):
                params['task_status'] = self.task_status.to_alipay_dict()
            else:
                params['task_status'] = self.task_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CorpusPublishTaskResult()
        if 'corpus_type' in d:
            o.corpus_type = d['corpus_type']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'process_success_count' in d:
            o.process_success_count = d['process_success_count']
        if 'process_total_count' in d:
            o.process_total_count = d['process_total_count']
        if 'publish_name' in d:
            o.publish_name = d['publish_name']
        if 'publish_type' in d:
            o.publish_type = d['publish_type']
        if 'task_status' in d:
            o.task_status = d['task_status']
        return o


