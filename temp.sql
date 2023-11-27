-- 사용자 정보 Table
CREATE TABLE auth.t_user (
    id BIGINT(20) AUTO_INCREMENT PRIMARY KEY,
    login_id VARCHAR(255) UNIQUE NOT NULL COMMENT '사용자 접속 ID',
    name VARCHAR(255) NOT NULL COMMENT '사용자 명',
    password VARCHAR(255) NOT NULL COMMENT '사용자 패스워드',
    provider_type VARCHAR(255) NOT NULL DEFAULT 'HOMEPAGE' COMMENT '
        Enum의 Default의 경우에는 값을 넣어줘야 하며, 연결이 되진 않습니다.
        기본 가입은 HOMEPAGE로 생각합니다.
    ',
    role VARCHAR(255) NOT NULL DEFAULT 'USER' COMMENT '사용자 Role',
    status VARCHAR(255) NOT NULL DEFAULT 'WAITING' COMMENT '사용자 계정 상태',
    mvp_level VARCHAR(255) NOT NULL DEFAULT 'BRONZE' COMMENT '사용자 결제 상태',
    email VARCHAR(255) COMMENT '사용자 메일',
    login_at DATETIME(6) DEFAULT CURRENT_TIMESTAMP COMMENT '마지막 로그인',
    lock_count INT DEFAULT 0 COMMENT '로그인 실패 횟수',
    created_at DATETIME(6) DEFAULT CURRENT_TIMESTAMP COMMENT '계정 생성일',
    updated_at DATETIME(6) DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '계정 정보 최종 수정일',
    updated_user BIGINT(20) COMMENT '
        auth.t_user.id를 OneToMany로 관계한다. 관리자 수정을 통해 여러명이 나올 수 있기 때문
        최종 계정 정보 수정자, 해당 정보는 관리자가 수정 할 수도 있으므로...
    ',
    INDEX t_user_id_status_idx (id, status) COMMENT '계정 가입순서, 상태로 인덱싱, 상태값을 기준으로 찾을일이 많으므로..'
);

-- 사용자의 프로필 이미지 Resource Mapping Table
CREATE TABLE auth.t_user_profile_resource (
    user_id BIGINT(20) REFERENCES auth.t_user(id) NOT NULL COMMENT '사용자 ID',
    resource_id BIGINT(20) REFERENCES common.tbl_resource(id) NOT NULL COMMENT 'Resource ID',
    PRIMARY KEY (user_id, resource_id),
    INDEX i_resource_user_id_order (user_id)
);

-- 사용자 정보 Table
CREATE TABLE auth.t_user_provider_key (
    id BIGINT(20) AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT(20) REFERENCES auth.t_user(id) NOT NULL COMMENT '사용자 계정 고유 ID',
    provider_type VARCHAR(255) NOT NULL COMMENT '
        auth.t_user정보를 그대로 가져온다. 꼭 필요하진 않은 컬럼이고 조인해서 가져와도 좋을듯함
    ',
    refresh_token VARCHAR(255) NOT NULL COMMENT '사용자 refresh Token Value',
    expired_time DATETIME NOT NULL COMMENT '
        provider에서 받은 payload영역의 expired_date시간
    ',
    need_delete TINYINT(1) DEFAULT 0 COMMENT '
        삭제 필요 여부, 0:미삭제, 1:삭제 , expired_time이 Over되면 true로 바꾸고 특정 시간에 batch로 전체 Delete
    ',
    INDEX i_provider_key_default_idx (id, user_id, provider_type),
    INDEX i_provider_key_delete_order (need_delete)
);
