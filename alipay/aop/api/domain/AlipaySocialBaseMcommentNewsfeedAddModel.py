#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NewsfeedMediaGiftInfo import NewsfeedMediaGiftInfo
from alipay.aop.api.domain.NewsfeedMediaImg import NewsfeedMediaImg
from alipay.aop.api.domain.NewsfeedLabelInfo import NewsfeedLabelInfo
from alipay.aop.api.domain.NewsfeedMediaLinkInfo import NewsfeedMediaLinkInfo
from alipay.aop.api.domain.NewsfeedLocationInfo import NewsfeedLocationInfo
from alipay.aop.api.domain.NewsfeedMediaVideoInfo import NewsfeedMediaVideoInfo
from alipay.aop.api.domain.NewsfeedWithMeInfo import NewsfeedWithMeInfo


class AlipaySocialBaseMcommentNewsfeedAddModel(object):

    def __init__(self):
        self._activity_address = None
        self._activity_name = None
        self._aid = None
        self._biz_no = None
        self._content = None
        self._gift_info = None
        self._img_infos = None
        self._label_info = None
        self._link_info = None
        self._location_info = None
        self._location_name = None
        self._location_scheme = None
        self._scene_code = None
        self._score = None
        self._source = None
        self._source_icon = None
        self._source_name = None
        self._spread_range = None
        self._type = None
        self._user_id = None
        self._video_info = None
        self._visible = None
        self._visible_range = None
        self._with_me = None

    @property
    def activity_address(self):
        return self._activity_address

    @activity_address.setter
    def activity_address(self, value):
        self._activity_address = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def aid(self):
        return self._aid

    @aid.setter
    def aid(self, value):
        self._aid = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def gift_info(self):
        return self._gift_info

    @gift_info.setter
    def gift_info(self, value):
        if isinstance(value, NewsfeedMediaGiftInfo):
            self._gift_info = value
        else:
            self._gift_info = NewsfeedMediaGiftInfo.from_alipay_dict(value)
    @property
    def img_infos(self):
        return self._img_infos

    @img_infos.setter
    def img_infos(self, value):
        if isinstance(value, list):
            self._img_infos = list()
            for i in value:
                if isinstance(i, NewsfeedMediaImg):
                    self._img_infos.append(i)
                else:
                    self._img_infos.append(NewsfeedMediaImg.from_alipay_dict(i))
    @property
    def label_info(self):
        return self._label_info

    @label_info.setter
    def label_info(self, value):
        if isinstance(value, NewsfeedLabelInfo):
            self._label_info = value
        else:
            self._label_info = NewsfeedLabelInfo.from_alipay_dict(value)
    @property
    def link_info(self):
        return self._link_info

    @link_info.setter
    def link_info(self, value):
        if isinstance(value, NewsfeedMediaLinkInfo):
            self._link_info = value
        else:
            self._link_info = NewsfeedMediaLinkInfo.from_alipay_dict(value)
    @property
    def location_info(self):
        return self._location_info

    @location_info.setter
    def location_info(self, value):
        if isinstance(value, NewsfeedLocationInfo):
            self._location_info = value
        else:
            self._location_info = NewsfeedLocationInfo.from_alipay_dict(value)
    @property
    def location_name(self):
        return self._location_name

    @location_name.setter
    def location_name(self, value):
        self._location_name = value
    @property
    def location_scheme(self):
        return self._location_scheme

    @location_scheme.setter
    def location_scheme(self, value):
        self._location_scheme = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def source_icon(self):
        return self._source_icon

    @source_icon.setter
    def source_icon(self, value):
        self._source_icon = value
    @property
    def source_name(self):
        return self._source_name

    @source_name.setter
    def source_name(self, value):
        self._source_name = value
    @property
    def spread_range(self):
        return self._spread_range

    @spread_range.setter
    def spread_range(self, value):
        self._spread_range = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def video_info(self):
        return self._video_info

    @video_info.setter
    def video_info(self, value):
        if isinstance(value, NewsfeedMediaVideoInfo):
            self._video_info = value
        else:
            self._video_info = NewsfeedMediaVideoInfo.from_alipay_dict(value)
    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self._visible = value
    @property
    def visible_range(self):
        return self._visible_range

    @visible_range.setter
    def visible_range(self, value):
        if isinstance(value, list):
            self._visible_range = list()
            for i in value:
                self._visible_range.append(i)
    @property
    def with_me(self):
        return self._with_me

    @with_me.setter
    def with_me(self, value):
        if isinstance(value, list):
            self._with_me = list()
            for i in value:
                if isinstance(i, NewsfeedWithMeInfo):
                    self._with_me.append(i)
                else:
                    self._with_me.append(NewsfeedWithMeInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.activity_address:
            if hasattr(self.activity_address, 'to_alipay_dict'):
                params['activity_address'] = self.activity_address.to_alipay_dict()
            else:
                params['activity_address'] = self.activity_address
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.aid:
            if hasattr(self.aid, 'to_alipay_dict'):
                params['aid'] = self.aid.to_alipay_dict()
            else:
                params['aid'] = self.aid
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.gift_info:
            if hasattr(self.gift_info, 'to_alipay_dict'):
                params['gift_info'] = self.gift_info.to_alipay_dict()
            else:
                params['gift_info'] = self.gift_info
        if self.img_infos:
            if isinstance(self.img_infos, list):
                for i in range(0, len(self.img_infos)):
                    element = self.img_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.img_infos[i] = element.to_alipay_dict()
            if hasattr(self.img_infos, 'to_alipay_dict'):
                params['img_infos'] = self.img_infos.to_alipay_dict()
            else:
                params['img_infos'] = self.img_infos
        if self.label_info:
            if hasattr(self.label_info, 'to_alipay_dict'):
                params['label_info'] = self.label_info.to_alipay_dict()
            else:
                params['label_info'] = self.label_info
        if self.link_info:
            if hasattr(self.link_info, 'to_alipay_dict'):
                params['link_info'] = self.link_info.to_alipay_dict()
            else:
                params['link_info'] = self.link_info
        if self.location_info:
            if hasattr(self.location_info, 'to_alipay_dict'):
                params['location_info'] = self.location_info.to_alipay_dict()
            else:
                params['location_info'] = self.location_info
        if self.location_name:
            if hasattr(self.location_name, 'to_alipay_dict'):
                params['location_name'] = self.location_name.to_alipay_dict()
            else:
                params['location_name'] = self.location_name
        if self.location_scheme:
            if hasattr(self.location_scheme, 'to_alipay_dict'):
                params['location_scheme'] = self.location_scheme.to_alipay_dict()
            else:
                params['location_scheme'] = self.location_scheme
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.source_icon:
            if hasattr(self.source_icon, 'to_alipay_dict'):
                params['source_icon'] = self.source_icon.to_alipay_dict()
            else:
                params['source_icon'] = self.source_icon
        if self.source_name:
            if hasattr(self.source_name, 'to_alipay_dict'):
                params['source_name'] = self.source_name.to_alipay_dict()
            else:
                params['source_name'] = self.source_name
        if self.spread_range:
            if hasattr(self.spread_range, 'to_alipay_dict'):
                params['spread_range'] = self.spread_range.to_alipay_dict()
            else:
                params['spread_range'] = self.spread_range
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.video_info:
            if hasattr(self.video_info, 'to_alipay_dict'):
                params['video_info'] = self.video_info.to_alipay_dict()
            else:
                params['video_info'] = self.video_info
        if self.visible:
            if hasattr(self.visible, 'to_alipay_dict'):
                params['visible'] = self.visible.to_alipay_dict()
            else:
                params['visible'] = self.visible
        if self.visible_range:
            if isinstance(self.visible_range, list):
                for i in range(0, len(self.visible_range)):
                    element = self.visible_range[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.visible_range[i] = element.to_alipay_dict()
            if hasattr(self.visible_range, 'to_alipay_dict'):
                params['visible_range'] = self.visible_range.to_alipay_dict()
            else:
                params['visible_range'] = self.visible_range
        if self.with_me:
            if isinstance(self.with_me, list):
                for i in range(0, len(self.with_me)):
                    element = self.with_me[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.with_me[i] = element.to_alipay_dict()
            if hasattr(self.with_me, 'to_alipay_dict'):
                params['with_me'] = self.with_me.to_alipay_dict()
            else:
                params['with_me'] = self.with_me
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseMcommentNewsfeedAddModel()
        if 'activity_address' in d:
            o.activity_address = d['activity_address']
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'aid' in d:
            o.aid = d['aid']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'content' in d:
            o.content = d['content']
        if 'gift_info' in d:
            o.gift_info = d['gift_info']
        if 'img_infos' in d:
            o.img_infos = d['img_infos']
        if 'label_info' in d:
            o.label_info = d['label_info']
        if 'link_info' in d:
            o.link_info = d['link_info']
        if 'location_info' in d:
            o.location_info = d['location_info']
        if 'location_name' in d:
            o.location_name = d['location_name']
        if 'location_scheme' in d:
            o.location_scheme = d['location_scheme']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'score' in d:
            o.score = d['score']
        if 'source' in d:
            o.source = d['source']
        if 'source_icon' in d:
            o.source_icon = d['source_icon']
        if 'source_name' in d:
            o.source_name = d['source_name']
        if 'spread_range' in d:
            o.spread_range = d['spread_range']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'video_info' in d:
            o.video_info = d['video_info']
        if 'visible' in d:
            o.visible = d['visible']
        if 'visible_range' in d:
            o.visible_range = d['visible_range']
        if 'with_me' in d:
            o.with_me = d['with_me']
        return o


