#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ArticleAttachmentInfo import ArticleAttachmentInfo
from alipay.aop.api.domain.ArticleCategoryInfo import ArticleCategoryInfo
from alipay.aop.api.domain.ArticleAttachmentInfo import ArticleAttachmentInfo


class ArticleInfo(object):

    def __init__(self):
        self._attachments = None
        self._category_id = None
        self._category_name_path = None
        self._category_path = None
        self._content = None
        self._create_time = None
        self._creator_id = None
        self._extend_titles = None
        self._id = None
        self._keywords = None
        self._library_id = None
        self._order_no = None
        self._pictures = None
        self._publish_end = None
        self._publish_start = None
        self._scene_codes = None
        self._source = None
        self._status = None
        self._status_code = None
        self._title = None
        self._update_time = None
        self._updater_id = None
        self._updater_name = None

    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        if isinstance(value, list):
            self._attachments = list()
            for i in value:
                if isinstance(i, ArticleAttachmentInfo):
                    self._attachments.append(i)
                else:
                    self._attachments.append(ArticleAttachmentInfo.from_alipay_dict(i))
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def category_name_path(self):
        return self._category_name_path

    @category_name_path.setter
    def category_name_path(self, value):
        self._category_name_path = value
    @property
    def category_path(self):
        return self._category_path

    @category_path.setter
    def category_path(self, value):
        if isinstance(value, list):
            self._category_path = list()
            for i in value:
                if isinstance(i, ArticleCategoryInfo):
                    self._category_path.append(i)
                else:
                    self._category_path.append(ArticleCategoryInfo.from_alipay_dict(i))
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
    def creator_id(self):
        return self._creator_id

    @creator_id.setter
    def creator_id(self, value):
        self._creator_id = value
    @property
    def extend_titles(self):
        return self._extend_titles

    @extend_titles.setter
    def extend_titles(self, value):
        if isinstance(value, list):
            self._extend_titles = list()
            for i in value:
                self._extend_titles.append(i)
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def keywords(self):
        return self._keywords

    @keywords.setter
    def keywords(self, value):
        if isinstance(value, list):
            self._keywords = list()
            for i in value:
                self._keywords.append(i)
    @property
    def library_id(self):
        return self._library_id

    @library_id.setter
    def library_id(self, value):
        self._library_id = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def pictures(self):
        return self._pictures

    @pictures.setter
    def pictures(self, value):
        if isinstance(value, list):
            self._pictures = list()
            for i in value:
                if isinstance(i, ArticleAttachmentInfo):
                    self._pictures.append(i)
                else:
                    self._pictures.append(ArticleAttachmentInfo.from_alipay_dict(i))
    @property
    def publish_end(self):
        return self._publish_end

    @publish_end.setter
    def publish_end(self, value):
        self._publish_end = value
    @property
    def publish_start(self):
        return self._publish_start

    @publish_start.setter
    def publish_start(self, value):
        self._publish_start = value
    @property
    def scene_codes(self):
        return self._scene_codes

    @scene_codes.setter
    def scene_codes(self, value):
        if isinstance(value, list):
            self._scene_codes = list()
            for i in value:
                self._scene_codes.append(i)
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value
    @property
    def updater_id(self):
        return self._updater_id

    @updater_id.setter
    def updater_id(self, value):
        self._updater_id = value
    @property
    def updater_name(self):
        return self._updater_name

    @updater_name.setter
    def updater_name(self, value):
        self._updater_name = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.category_name_path:
            if hasattr(self.category_name_path, 'to_alipay_dict'):
                params['category_name_path'] = self.category_name_path.to_alipay_dict()
            else:
                params['category_name_path'] = self.category_name_path
        if self.category_path:
            if isinstance(self.category_path, list):
                for i in range(0, len(self.category_path)):
                    element = self.category_path[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_path[i] = element.to_alipay_dict()
            if hasattr(self.category_path, 'to_alipay_dict'):
                params['category_path'] = self.category_path.to_alipay_dict()
            else:
                params['category_path'] = self.category_path
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
        if self.creator_id:
            if hasattr(self.creator_id, 'to_alipay_dict'):
                params['creator_id'] = self.creator_id.to_alipay_dict()
            else:
                params['creator_id'] = self.creator_id
        if self.extend_titles:
            if isinstance(self.extend_titles, list):
                for i in range(0, len(self.extend_titles)):
                    element = self.extend_titles[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.extend_titles[i] = element.to_alipay_dict()
            if hasattr(self.extend_titles, 'to_alipay_dict'):
                params['extend_titles'] = self.extend_titles.to_alipay_dict()
            else:
                params['extend_titles'] = self.extend_titles
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.keywords:
            if isinstance(self.keywords, list):
                for i in range(0, len(self.keywords)):
                    element = self.keywords[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.keywords[i] = element.to_alipay_dict()
            if hasattr(self.keywords, 'to_alipay_dict'):
                params['keywords'] = self.keywords.to_alipay_dict()
            else:
                params['keywords'] = self.keywords
        if self.library_id:
            if hasattr(self.library_id, 'to_alipay_dict'):
                params['library_id'] = self.library_id.to_alipay_dict()
            else:
                params['library_id'] = self.library_id
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.pictures:
            if isinstance(self.pictures, list):
                for i in range(0, len(self.pictures)):
                    element = self.pictures[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pictures[i] = element.to_alipay_dict()
            if hasattr(self.pictures, 'to_alipay_dict'):
                params['pictures'] = self.pictures.to_alipay_dict()
            else:
                params['pictures'] = self.pictures
        if self.publish_end:
            if hasattr(self.publish_end, 'to_alipay_dict'):
                params['publish_end'] = self.publish_end.to_alipay_dict()
            else:
                params['publish_end'] = self.publish_end
        if self.publish_start:
            if hasattr(self.publish_start, 'to_alipay_dict'):
                params['publish_start'] = self.publish_start.to_alipay_dict()
            else:
                params['publish_start'] = self.publish_start
        if self.scene_codes:
            if isinstance(self.scene_codes, list):
                for i in range(0, len(self.scene_codes)):
                    element = self.scene_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scene_codes[i] = element.to_alipay_dict()
            if hasattr(self.scene_codes, 'to_alipay_dict'):
                params['scene_codes'] = self.scene_codes.to_alipay_dict()
            else:
                params['scene_codes'] = self.scene_codes
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_code:
            if hasattr(self.status_code, 'to_alipay_dict'):
                params['status_code'] = self.status_code.to_alipay_dict()
            else:
                params['status_code'] = self.status_code
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        if self.updater_id:
            if hasattr(self.updater_id, 'to_alipay_dict'):
                params['updater_id'] = self.updater_id.to_alipay_dict()
            else:
                params['updater_id'] = self.updater_id
        if self.updater_name:
            if hasattr(self.updater_name, 'to_alipay_dict'):
                params['updater_name'] = self.updater_name.to_alipay_dict()
            else:
                params['updater_name'] = self.updater_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ArticleInfo()
        if 'attachments' in d:
            o.attachments = d['attachments']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'category_name_path' in d:
            o.category_name_path = d['category_name_path']
        if 'category_path' in d:
            o.category_path = d['category_path']
        if 'content' in d:
            o.content = d['content']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'creator_id' in d:
            o.creator_id = d['creator_id']
        if 'extend_titles' in d:
            o.extend_titles = d['extend_titles']
        if 'id' in d:
            o.id = d['id']
        if 'keywords' in d:
            o.keywords = d['keywords']
        if 'library_id' in d:
            o.library_id = d['library_id']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'pictures' in d:
            o.pictures = d['pictures']
        if 'publish_end' in d:
            o.publish_end = d['publish_end']
        if 'publish_start' in d:
            o.publish_start = d['publish_start']
        if 'scene_codes' in d:
            o.scene_codes = d['scene_codes']
        if 'source' in d:
            o.source = d['source']
        if 'status' in d:
            o.status = d['status']
        if 'status_code' in d:
            o.status_code = d['status_code']
        if 'title' in d:
            o.title = d['title']
        if 'update_time' in d:
            o.update_time = d['update_time']
        if 'updater_id' in d:
            o.updater_id = d['updater_id']
        if 'updater_name' in d:
            o.updater_name = d['updater_name']
        return o


