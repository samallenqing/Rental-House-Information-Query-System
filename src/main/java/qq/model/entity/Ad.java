package qq.model.entity;


import lombok.Data;

import javax.persistence.*;

@Data
@Entity
@Table(name = "ad")
public class Ad {
    @Id
    @Column(name = "adid")
    Long adId;
    @Column(name = "zipcode")
    String zipCode;
    String location;
    int price;
    String model;
    String url;
    String gps;
    String description;
}
