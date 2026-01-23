#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AIStreamContent import AIStreamContent


class StreamResponse(object):

    def __init__(self):
        self._agent_id = None
        self._biz_info = None
        self._chat_id = None
        self._contents = None
        self._out_biz_content = None
        self._session_id = None
        self._show_contents = None
        self._turn = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        self._biz_info = value
    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, value):
        if isinstance(value, list):
            self._contents = list()
            for i in value:
                if isinstance(i, AIStreamContent):
                    self._contents.append(i)
                else:
                    self._contents.append(AIStreamContent.from_alipay_dict(i))
    @property
    def out_biz_content(self):
        return self._out_biz_content

    @out_biz_content.setter
    def out_biz_content(self, value):
        self._out_biz_content = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def show_contents(self):
        return self._show_contents

    @show_contents.setter
    def show_contents(self, value):
        self._show_contents = value
    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, value):
        self._turn = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.biz_info:
            if hasattr(self.biz_info, 'to_alipay_dict'):
                params['biz_info'] = self.biz_info.to_alipay_dict()
            else:
                params['biz_info'] = self.biz_info
        if self.chat_id:
            if hasattr(self.chat_id, 'to_alipay_dict'):
                params['chat_id'] = self.chat_id.to_alipay_dict()
            else:
                params['chat_id'] = self.chat_id
        if self.contents:
            if isinstance(self.contents, list):
                for i in range(0, len(self.contents)):
                    element = self.contents[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contents[i] = element.to_alipay_dict()
            if hasattr(self.contents, 'to_alipay_dict'):
                params['contents'] = self.contents.to_alipay_dict()
            else:
                params['contents'] = self.contents
        if self.out_biz_content:
            if hasattr(self.out_biz_content, 'to_alipay_dict'):
                params['out_biz_content'] = self.out_biz_content.to_alipay_dict()
            else:
                params['out_biz_content'] = self.out_biz_content
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.show_contents:
            if hasattr(self.show_contents, 'to_alipay_dict'):
                params['show_contents'] = self.show_contents.to_alipay_dict()
            else:
                params['show_contents'] = self.show_contents
        if self.turn:
            if hasattr(self.turn, 'to_alipay_dict'):
                params['turn'] = self.turn.to_alipay_dict()
            else:
                params['turn'] = self.turn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StreamResponse()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'biz_info' in d:
            o.biz_info = d['biz_info']
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'contents' in d:
            o.contents = d['contents']
        if 'out_biz_content' in d:
            o.out_biz_content = d['out_biz_content']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'show_contents' in d:
            o.show_contents = d['show_contents']
        if 'turn' in d:
            o.turn = d['turn']
        return o


