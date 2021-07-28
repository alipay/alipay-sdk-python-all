#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ArticleAttachmentInfo import ArticleAttachmentInfo
from alipay.aop.api.domain.ArticleCategoryInfo import ArticleCategoryInfo
from alipay.aop.api.domain.ArticleAttachmentInfo import ArticleAttachmentInfo


class AlipayIserviceCcmSwArticleGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmSwArticleGetResponse, self).__init__()
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

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmSwArticleGetResponse, self).parse_response_content(response_content)
        if 'attachments' in response:
            self.attachments = response['attachments']
        if 'category_id' in response:
            self.category_id = response['category_id']
        if 'category_name_path' in response:
            self.category_name_path = response['category_name_path']
        if 'category_path' in response:
            self.category_path = response['category_path']
        if 'content' in response:
            self.content = response['content']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'creator_id' in response:
            self.creator_id = response['creator_id']
        if 'extend_titles' in response:
            self.extend_titles = response['extend_titles']
        if 'id' in response:
            self.id = response['id']
        if 'keywords' in response:
            self.keywords = response['keywords']
        if 'library_id' in response:
            self.library_id = response['library_id']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'pictures' in response:
            self.pictures = response['pictures']
        if 'publish_end' in response:
            self.publish_end = response['publish_end']
        if 'publish_start' in response:
            self.publish_start = response['publish_start']
        if 'scene_codes' in response:
            self.scene_codes = response['scene_codes']
        if 'source' in response:
            self.source = response['source']
        if 'status' in response:
            self.status = response['status']
        if 'status_code' in response:
            self.status_code = response['status_code']
        if 'title' in response:
            self.title = response['title']
        if 'update_time' in response:
            self.update_time = response['update_time']
        if 'updater_id' in response:
            self.updater_id = response['updater_id']
        if 'updater_name' in response:
            self.updater_name = response['updater_name']
