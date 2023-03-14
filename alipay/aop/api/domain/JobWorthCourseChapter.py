#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JobWorthCourseChapter(object):

    def __init__(self):
        self._chapter_no = None
        self._content_type = None
        self._course_chapter_id = None
        self._name = None
        self._node_type = None
        self._parent_chapter_id = None
        self._video_content_id = None

    @property
    def chapter_no(self):
        return self._chapter_no

    @chapter_no.setter
    def chapter_no(self, value):
        self._chapter_no = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def course_chapter_id(self):
        return self._course_chapter_id

    @course_chapter_id.setter
    def course_chapter_id(self, value):
        self._course_chapter_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def node_type(self):
        return self._node_type

    @node_type.setter
    def node_type(self, value):
        self._node_type = value
    @property
    def parent_chapter_id(self):
        return self._parent_chapter_id

    @parent_chapter_id.setter
    def parent_chapter_id(self, value):
        self._parent_chapter_id = value
    @property
    def video_content_id(self):
        return self._video_content_id

    @video_content_id.setter
    def video_content_id(self, value):
        self._video_content_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.chapter_no:
            if hasattr(self.chapter_no, 'to_alipay_dict'):
                params['chapter_no'] = self.chapter_no.to_alipay_dict()
            else:
                params['chapter_no'] = self.chapter_no
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.course_chapter_id:
            if hasattr(self.course_chapter_id, 'to_alipay_dict'):
                params['course_chapter_id'] = self.course_chapter_id.to_alipay_dict()
            else:
                params['course_chapter_id'] = self.course_chapter_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.node_type:
            if hasattr(self.node_type, 'to_alipay_dict'):
                params['node_type'] = self.node_type.to_alipay_dict()
            else:
                params['node_type'] = self.node_type
        if self.parent_chapter_id:
            if hasattr(self.parent_chapter_id, 'to_alipay_dict'):
                params['parent_chapter_id'] = self.parent_chapter_id.to_alipay_dict()
            else:
                params['parent_chapter_id'] = self.parent_chapter_id
        if self.video_content_id:
            if hasattr(self.video_content_id, 'to_alipay_dict'):
                params['video_content_id'] = self.video_content_id.to_alipay_dict()
            else:
                params['video_content_id'] = self.video_content_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JobWorthCourseChapter()
        if 'chapter_no' in d:
            o.chapter_no = d['chapter_no']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'course_chapter_id' in d:
            o.course_chapter_id = d['course_chapter_id']
        if 'name' in d:
            o.name = d['name']
        if 'node_type' in d:
            o.node_type = d['node_type']
        if 'parent_chapter_id' in d:
            o.parent_chapter_id = d['parent_chapter_id']
        if 'video_content_id' in d:
            o.video_content_id = d['video_content_id']
        return o


