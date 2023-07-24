#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAntbookcontentChapterSyncModel(object):

    def __init__(self):
        self._book_id = None
        self._chapter_free = None
        self._chapter_id = None
        self._content = None
        self._create_time = None
        self._last_audit_time = None
        self._name = None
        self._operate_type = None
        self._shelves_time = None
        self._sort_no = None
        self._tag_list = None
        self._text_format = None
        self._update_time = None
        self._volume_id = None
        self._word_number = None

    @property
    def book_id(self):
        return self._book_id

    @book_id.setter
    def book_id(self, value):
        self._book_id = value
    @property
    def chapter_free(self):
        return self._chapter_free

    @chapter_free.setter
    def chapter_free(self, value):
        self._chapter_free = value
    @property
    def chapter_id(self):
        return self._chapter_id

    @chapter_id.setter
    def chapter_id(self, value):
        self._chapter_id = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def last_audit_time(self):
        return self._last_audit_time

    @last_audit_time.setter
    def last_audit_time(self, value):
        self._last_audit_time = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def shelves_time(self):
        return self._shelves_time

    @shelves_time.setter
    def shelves_time(self, value):
        self._shelves_time = value
    @property
    def sort_no(self):
        return self._sort_no

    @sort_no.setter
    def sort_no(self, value):
        self._sort_no = value
    @property
    def tag_list(self):
        return self._tag_list

    @tag_list.setter
    def tag_list(self, value):
        if isinstance(value, list):
            self._tag_list = list()
            for i in value:
                self._tag_list.append(i)
    @property
    def text_format(self):
        return self._text_format

    @text_format.setter
    def text_format(self, value):
        self._text_format = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value
    @property
    def volume_id(self):
        return self._volume_id

    @volume_id.setter
    def volume_id(self, value):
        self._volume_id = value
    @property
    def word_number(self):
        return self._word_number

    @word_number.setter
    def word_number(self, value):
        self._word_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.book_id:
            if hasattr(self.book_id, 'to_alipay_dict'):
                params['book_id'] = self.book_id.to_alipay_dict()
            else:
                params['book_id'] = self.book_id
        if self.chapter_free:
            if hasattr(self.chapter_free, 'to_alipay_dict'):
                params['chapter_free'] = self.chapter_free.to_alipay_dict()
            else:
                params['chapter_free'] = self.chapter_free
        if self.chapter_id:
            if hasattr(self.chapter_id, 'to_alipay_dict'):
                params['chapter_id'] = self.chapter_id.to_alipay_dict()
            else:
                params['chapter_id'] = self.chapter_id
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.last_audit_time:
            if hasattr(self.last_audit_time, 'to_alipay_dict'):
                params['last_audit_time'] = self.last_audit_time.to_alipay_dict()
            else:
                params['last_audit_time'] = self.last_audit_time
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.shelves_time:
            if hasattr(self.shelves_time, 'to_alipay_dict'):
                params['shelves_time'] = self.shelves_time.to_alipay_dict()
            else:
                params['shelves_time'] = self.shelves_time
        if self.sort_no:
            if hasattr(self.sort_no, 'to_alipay_dict'):
                params['sort_no'] = self.sort_no.to_alipay_dict()
            else:
                params['sort_no'] = self.sort_no
        if self.tag_list:
            if isinstance(self.tag_list, list):
                for i in range(0, len(self.tag_list)):
                    element = self.tag_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_list[i] = element.to_alipay_dict()
            if hasattr(self.tag_list, 'to_alipay_dict'):
                params['tag_list'] = self.tag_list.to_alipay_dict()
            else:
                params['tag_list'] = self.tag_list
        if self.text_format:
            if hasattr(self.text_format, 'to_alipay_dict'):
                params['text_format'] = self.text_format.to_alipay_dict()
            else:
                params['text_format'] = self.text_format
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        if self.volume_id:
            if hasattr(self.volume_id, 'to_alipay_dict'):
                params['volume_id'] = self.volume_id.to_alipay_dict()
            else:
                params['volume_id'] = self.volume_id
        if self.word_number:
            if hasattr(self.word_number, 'to_alipay_dict'):
                params['word_number'] = self.word_number.to_alipay_dict()
            else:
                params['word_number'] = self.word_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAntbookcontentChapterSyncModel()
        if 'book_id' in d:
            o.book_id = d['book_id']
        if 'chapter_free' in d:
            o.chapter_free = d['chapter_free']
        if 'chapter_id' in d:
            o.chapter_id = d['chapter_id']
        if 'content' in d:
            o.content = d['content']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'last_audit_time' in d:
            o.last_audit_time = d['last_audit_time']
        if 'name' in d:
            o.name = d['name']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'shelves_time' in d:
            o.shelves_time = d['shelves_time']
        if 'sort_no' in d:
            o.sort_no = d['sort_no']
        if 'tag_list' in d:
            o.tag_list = d['tag_list']
        if 'text_format' in d:
            o.text_format = d['text_format']
        if 'update_time' in d:
            o.update_time = d['update_time']
        if 'volume_id' in d:
            o.volume_id = d['volume_id']
        if 'word_number' in d:
            o.word_number = d['word_number']
        return o


