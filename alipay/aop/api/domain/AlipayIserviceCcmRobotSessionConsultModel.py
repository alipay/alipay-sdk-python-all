#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BizInfo import BizInfo


class AlipayIserviceCcmRobotSessionConsultModel(object):

    def __init__(self):
        self._biz_info = None
        self._document_ids = None
        self._knowledge_id = None
        self._query = None
        self._robot_code = None
        self._scene_code = None
        self._session_id = None
        self._visitor_id = None

    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        if isinstance(value, BizInfo):
            self._biz_info = value
        else:
            self._biz_info = BizInfo.from_alipay_dict(value)
    @property
    def document_ids(self):
        return self._document_ids

    @document_ids.setter
    def document_ids(self, value):
        self._document_ids = value
    @property
    def knowledge_id(self):
        return self._knowledge_id

    @knowledge_id.setter
    def knowledge_id(self, value):
        self._knowledge_id = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def robot_code(self):
        return self._robot_code

    @robot_code.setter
    def robot_code(self, value):
        self._robot_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def visitor_id(self):
        return self._visitor_id

    @visitor_id.setter
    def visitor_id(self, value):
        self._visitor_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_info:
            if hasattr(self.biz_info, 'to_alipay_dict'):
                params['biz_info'] = self.biz_info.to_alipay_dict()
            else:
                params['biz_info'] = self.biz_info
        if self.document_ids:
            if hasattr(self.document_ids, 'to_alipay_dict'):
                params['document_ids'] = self.document_ids.to_alipay_dict()
            else:
                params['document_ids'] = self.document_ids
        if self.knowledge_id:
            if hasattr(self.knowledge_id, 'to_alipay_dict'):
                params['knowledge_id'] = self.knowledge_id.to_alipay_dict()
            else:
                params['knowledge_id'] = self.knowledge_id
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.robot_code:
            if hasattr(self.robot_code, 'to_alipay_dict'):
                params['robot_code'] = self.robot_code.to_alipay_dict()
            else:
                params['robot_code'] = self.robot_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.visitor_id:
            if hasattr(self.visitor_id, 'to_alipay_dict'):
                params['visitor_id'] = self.visitor_id.to_alipay_dict()
            else:
                params['visitor_id'] = self.visitor_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmRobotSessionConsultModel()
        if 'biz_info' in d:
            o.biz_info = d['biz_info']
        if 'document_ids' in d:
            o.document_ids = d['document_ids']
        if 'knowledge_id' in d:
            o.knowledge_id = d['knowledge_id']
        if 'query' in d:
            o.query = d['query']
        if 'robot_code' in d:
            o.robot_code = d['robot_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'visitor_id' in d:
            o.visitor_id = d['visitor_id']
        return o


